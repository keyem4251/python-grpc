import os

from flask import Flask, render_template, session, redirect, url_for, request
import grpc

from recommendations_pb2 import (
    BookCategory,
    RecommendationRequest,
    RecommendationResponse,
)
from recommendations_pb2_grpc import RecommendationsStub

from inventory_pb2_grpc import InventoryStub
from auth import init_auth

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)

inventory_host = os.getenv("INVENTORY_HOST", "localhost")
inventory_channel = grpc.insecure_channel(f"{inventory_host}:50052")
inventory_client = InventoryStub(inventory_channel)


@app.route("/", methods=["GET"])
def render_homepage():
    user = session.get("user")
    if user is None:
        return redirect(url_for("login"))

    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    response: RecommendationResponse = recommendations_client.Recommend(request)

    books = inventory_client.List()

    return render_template(
        "homepage.html",
        recommendations=response.recommendations,
        books=books
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", msg="")

    email = request.form["email"]
    password = request.form["password"]
    auth = init_auth()
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        session["user"] = email
        return redirect(url_for("render_homepage"))
    except:
        return render_template("login.html", msg="メールアドレスまたはパスワードが間違っています。")


@app.route("/logout")
def logout():
    del session["user"]
    return redirect(url_for("login"))
