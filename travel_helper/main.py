from travel_helper.recommender import recommend_destination

def main():
    destination = recommend_destination()
    print(f"Recommended destination: {destination}")

if __name__ == "__main__":
  main()