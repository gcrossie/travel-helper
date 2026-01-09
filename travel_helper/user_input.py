# travel_helper/user_input.py

def ask_choice(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")


def ask_multi_choice(prompt, options, allow_single=True):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            raw = input("Enter your choices (comma-separated): ")
            choices = [int(c.strip()) for c in raw.split(",") if c.strip().isdigit()]

            if not choices and not allow_single:
                print("At least one choice is required.")
                continue

            if not all(1 <= c <= len(options) for c in choices):
                print("Invalid choice(s). Please try again.")
                continue

            return [options[c - 1] for c in choices]
        except ValueError:
            print("Please enter numbers only.")
