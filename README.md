# Travel Helper

Travel Helper is a command-line Python application that recommends a travel destination based on user preferences such as trip type, temperature, travel duration, and activities.

The purpose of this project is to demonstrate a clear Python project structure, modular code, use of a class, dependency management with requirements.txt, and basic Git workflow.

---

# Features

- Interactive command-line interface
- Destination recommendation based on:
  - Trip type (city, nature)
  - Preferred temperature (cold, mild, warm)
  - Travel duration (short, week, long)
  - Activities (single or multiple choice)
- Recommendation logic handled by a class
- Modular Python files
- Custom logger (logs to console and file)
- Dependency management via requirements.txt

---

# Project Structure

```text
travel-helper/
├── travel_helper/
│   ├── main.py
│   ├── recommender.py
│   ├── processor.py
│   ├── user_input.py
│   ├── utils/
│   │   ├── logger.py
│   │   ├── config.py
│   │   └── __init__.py
│   └── __init__.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/        # local virtual environment (not tracked by git)
```

---

# Installation

1. Clone the repository:
git clone https://github.com/gcrossie/travel-helper.git
cd travel-helper

2. Create a virtual environment:
python -m venv venv

3. Activate the virtual environment:

Windows (Git Bash / Hyper):
source venv/Scripts/activate

macOS / Linux:
source venv/bin/activate

4. Install dependencies:
python -m pip install -r requirements.txt

---

# Usage

Run the application from the project root:

python -m travel_helper.main

Follow the on-screen prompts to receive a travel destination recommendation.

---

# Dependencies

All external dependencies are listed in requirements.txt.

- colorama

---

# Author

Gabriella Cross
