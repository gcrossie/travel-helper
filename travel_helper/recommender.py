# travel_helper/recommender.py

from typing import List
from travel_helper.processor import recommend_destination


class TravelRecommender:
    """
    Simple wrapper class for destination recommendation logic.
    Exists to satisfy the requirement of using at least one class.
    """

    def recommend(
        self,
        trip_type: str,
        temperature: str,
        duration: str,
        activities: List[str],
    ) -> str:
        return recommend_destination(
            trip_type=trip_type,
            temperature=temperature,
            duration=duration,
            activities=activities,
        )

