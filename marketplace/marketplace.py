import os

from flask import Flask, render_template, session, redirect, url_for, request
import grpc

from recommendations_pb2 import (
    BookCategory,
    RecommendationRequest,
    RecommendationResponse,
)
from recommendations_pb2_grpc import RecommendationsStub
from auth_pb2 import (
    HelloRequest,
    HelloResponse,
)
from auth_pb2_grpc import GreeterStub
from auth import init_auth

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)

auth_host = os.getenv("AUTH_HOST", "localhost")
auth_channel = grpc.insecure_channel(f"{auth_host}:50052")
auth_client = GreeterStub(auth_channel)

@app.route("/")
def render_homepage():
    user = session.get("user")
    if user is None:
        return redirect(url_for("login"))

    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    response: RecommendationResponse = recommendations_client.Recommend(request)

    auth_request = HelloRequest(name="World")
    auth_response = auth_client.SayHello(auth_request)

    return render_template("homepage.html", recommendations=response.recommendations, auth=auth_response)


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
        return redirect(url_for("/"))
    except:
        return render_template("login.html", msg="メールアドレスまたはパスワードが間違っています。")


@app.route("/logout")
def logout():
    del session["user"]
    return redirect(url_for("login"))
