# travel_helper/processor.py

from __future__ import annotations
import random

DESTINATIONS = [
    {
        "name": "Dolomites",
        "type": "nature",
        "temperature": "cold",
        "budget": "high",
        "duration": ["week", "long"],
        "activities": ["hiking", "relaxation"],
    },
    {
        "name": "Madeira",
        "type": "nature",
        "temperature": "mild",
        "budget": "medium",
        "duration": ["short", "week", "long"],
        "activities": ["hiking", "relaxation", "beach"],
    },
    {
        "name": "Osaka",
        "type": "city",
        "temperature": "mild",
        "budget": "high",
        "duration": ["short", "week"],
        "activities": ["food", "nightlife", "museums"],
    },
    {
        "name": "Marrakech",
        "type": "city",
        "temperature": "warm",
        "budget": "medium",
        "duration": ["short", "week"],
        "activities": ["food", "museums"],
    },
    {
        "name": "Bled",
        "type": "nature",
        "temperature": "mild",
        "budget": "medium",
        "duration": ["short", "week"],
        "activities": ["hiking", "relaxation"],
    },
    {
        "name": "Ilulissat",
        "type": "nature",
        "temperature": "cold",
        "budget": "high",
        "duration": ["week"],
        "activities": ["hiking", "relaxation"],
    },
    {
        "name": "Bali",
        "type": "nature",
        "temperature": "warm",
        "budget": "medium",
        "duration": ["week", "long"],
        "activities": ["relaxation", "beach"],
    },
    {
        "name": "San José",
        "type": "city",
        "temperature": "warm",
        "budget": "medium",
        "duration": ["short", "week"],
        "activities": ["food", "museums"],
    },
    {
        "name": "Auckland",
        "type": "city",
        "temperature": "mild",
        "budget": "high",
        "duration": ["week", "long"],
        "activities": ["food", "museums", "relaxation"],
    },
    {
        "name": "Cape Town",
        "type": "city",
        "temperature": "warm",
        "budget": "medium",
        "duration": ["week", "long"],
        "activities": ["food", "nightlife", "museums"],
    },
    {
        "name": "Brussels",
        "type": "city",
        "temperature": "mild",
        "budget": "medium",
        "duration": ["short", "week"],
        "activities": ["food", "museums"],
    },
    {
        "name": "Panama City",
        "type": "city",
        "temperature": "warm",
        "budget": "medium",
        "duration": ["short", "week"],
        "activities": ["food", "nightlife"],
    },
]


def recommend_destination(
    trip_type: str,
    temperature: str,
    duration: str,
    activities: list[str],
) -> str:
    """
    Returns a recommended destination name.
    Uses strict matching first, then a best-effort fallback.
    """

    matches = []

    # --- Strict matching ---
    for dest in DESTINATIONS:
        if dest["type"] != trip_type:
            continue
        if dest["temperature"] != temperature:
            continue
        if duration not in dest["duration"]:
            continue

        if activities:
            if not any(a in dest["activities"] for a in activities):
                continue

        matches.append(dest)

    if matches:
        return random.choice(matches)["name"]

    # --- Fallback (best-effort match) ---
    scored = []
    for dest in DESTINATIONS:
        score = 0

        if dest["type"] == trip_type:
            score += 2
        if dest["temperature"] == temperature:
            score += 2
        if duration in dest["duration"]:
            score += 1

        score += len(set(activities).intersection(dest["activities"]))
        scored.append((score, dest))

    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[0][1]["name"]



