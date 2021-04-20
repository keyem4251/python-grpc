import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import (
    BookCategory,
    RecommendationRequest,
    RecommendationResponse,
)
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    response: RecommendationResponse = recommendations_client.Recommend(request)
    return render_template("homepage.html", recommendations=response.recommendations)
