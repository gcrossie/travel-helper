from colorama import Fore, init

from travel_helper.utils.logger import setup_logger
from travel_helper.user_input import ask_choice, ask_multi_choice
from travel_helper.processor import recommend_destination

# Initialize colorama
init(autoreset=True)


def main():
    logger = setup_logger("travel_helper")
    logger.info("Program started")

    print(Fore.CYAN + "🌍 Welcome to Travel Helper!")
    print("Answer a few questions and I will recommend a destination.\n")

    # 1. Trip type
    trip_type = ask_choice(
        prompt="What type of trip do you want?",
        options=["city", "nature"]
    )

    # 2. Temperature
    temperature = ask_choice(
        prompt="Preferred temperature?",
        options=["cold", "mild", "warm"]
    )

    # 3. Duration
    duration = ask_choice(
        prompt="How long is your trip? (short = 3–5 days, long = 2+ weeks)",
        options=["short", "week", "long"]
    )

    # 4. Activities (single or multiple)
    activities = ask_multi_choice(
        prompt="What activities are you interested in?",
        options=["food", "museums", "hiking", "relaxation", "nightlife", "beach"],
        allow_single=True
    )

    logger.info(
        f"User preferences: "
        f"type={trip_type}, "
        f"temp={temperature}, "
        f"duration={duration}, "
        f"activities={activities}"
    )

    destination = recommend_destination(
        trip_type=trip_type,
        temperature=temperature,
        duration=duration,
        activities=activities
    )

    print()
    print(Fore.GREEN + "Recommended destination:")
    if destination:
        print(Fore.GREEN + destination)
    else:
        print(Fore.RED + "No destination matched your preferences.")

    logger.info("Program finished")


if __name__ == "__main__":
    main()


