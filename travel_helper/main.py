from travel_helper.utils.logger import setup_logger
from travel_helper.recommender import recommend_destination

logger = setup_logger("main")

def main():
    logger.info("Program started")

    destination = recommend_destination()
    print(f"Recommended destination: {destination}")

    logger.info("Program finished")

if __name__ == "__main__":
  main()