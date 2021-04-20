from recommendations import RecommendationService

from recommendations_pb2 import BookCategory, RecommendationRequest


def test_recommendations():
    sercivice = RecommendationService()
    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=1
    )
    response = sercivice.Recommend(request, None)
    assert len(response.recommendations) == 1
