"""
habits = {
    "habit1": {
        "log": {"2025-12-2": "done", "2025-12-3": "done"},
        "type": "measurable, check"
        }
}


"""

import json
from datetime import datetime


def load_habits():
    """load habits from habits.json file"""
    try:
        with open("habits.json", "r") as file:
            habits = json.load(file)
        return habits
    # if the file is not found, return empty dictionary
    except FileNotFoundError:
        print("habits file not found, starting empty...")
        return {}
    # if the file is corrupted, return emtpy dictionary
    except json.JSONDecodeError:
        print("habits file in corrupted, starting empty...")
        return {}


def save_habits(habits):
    """save habits to habits.json file"""
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)


def update_habits(habits, today):
    """adds today entry in habits log"""
    for habit in habits:
        log = habits[habit]["log"]
        if today in log:
            continue

        log[today] = False
    return habits


def view_all_habits(habits):
    """list all habits with log"""
    print(50 * "=")
    for habit in habits:
        print(f"{habit}: ")
        log = habits[habit]["log"]
        for date in log:
            print(f"{date}: {log[date]}")
        print(50 * "=")


def add_new_habit(habits, today):
    """add new habit to habits, return updated habits"""
    habit_name = input("Enter the habit name: ")
    # if the habit already exists, don't update habits
    if habit_name in habits:
        print("This habit already exists!")
        return habits

    habits[habit_name] = {"log": {today: False}}

    return habits


def mark_habit_as_done(habits, today):
    """update 'done' to True for a today"""
    habit_name = input("Enter the habit name: ")

    # if the habit doesn't exist, don't change habits
    if habit_name not in habits:
        print("Habit doesn't exist")
        return habits

    # update the habit
    habits[habit_name]["log"][today] = True
    return habits


# variables
today = datetime.now().strftime("%Y-%m-%d")

# load habits from habits.json file
habits = load_habits()

update_habits(habits, today)
save_habits(habits)

# main program
while True:
    # get the user input
    print(
        "Chose what to do:",
        "[1] View all habits",
        "[2] Add new habit",
        "[3] Mark habit as done",
        sep="\n",
    )
    user_input = input(">>> ")

    # main logic
    if user_input == "1":
        view_all_habits(habits)
    elif user_input == "2":
        habits = add_new_habit(habits, today)
        save_habits(habits)
    elif user_input == "3":
        habits = mark_habit_as_done(habits, today)
        save_habits(habits)
