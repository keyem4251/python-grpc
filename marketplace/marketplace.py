import os

from flask import Flask, render_template
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

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)

auth_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
auth_channel = grpc.insecure_channel(f"{auth_host}:50052")
auth_client = GreeterStub(auth_channel)

@app.route("/")
def render_homepage():
    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    response: RecommendationResponse = recommendations_client.Recommend(request)

    auth_request = HelloRequest(name="World")
    auth_response = auth_client.SayHello(auth_request)

    return render_template("homepage.html", recommendations=response.recommendations, auth=auth_response)
