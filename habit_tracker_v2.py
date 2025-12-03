import json
import os
from datetime import datetime


def load_habits():
    """load habits from habits.json file"""
    # load the habits
    try:
        with open("habits.json", "r") as file:
            habits = json.load(file)
        return habits
    # if the file not exists
    except FileNotFoundError:
        print("Habits file not found, starting empty...")
        return {}
    # if the file is corrupted
    except json.JSONDecodeError:
        print("Habits file is corrupted, starting empty...")
        return {}


def save_habits(habits):
    """save habits to habits.json file"""
    # save the habits
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)


def update_habits(habits, date):
    """automatically add new entry to habits log with the date of today with default value False or 0.0"""
    for habit in habits:
        habit_type = habits[habit]["type"]
        log = habits[habit]["log"]

        # if the date already exists, continue to the next habit
        if date in log:
            continue

        if habit_type == "check":
            log[today] = False
        elif habit_type == "measurable":
            log[today] = 0.0
        else:
            print(f"update habit failed. habit [{habit}] type is not known.")
            return habits

        habits[habit]["log"] = log

        return habits


def view_all_habits_today(habits):
    """list habits name and today value."""
    # decorate
    print(50 * "=")
    print("Habit        Today")
    print(50 * "=")

    # list today values only
    for habit in habits:
        print(f"{habit}         {habits[habit]['log'][today]}")

    print(50 * "=")


def add_new_habit(habits, today):
    """add new habit to habits, then return updated habits"""
    habit_name = input("Enter the habit name: ")

    # check if habit already exists
    if habit_name in habits:
        print("This habit already exists!")
        return habits

    habit_type = input("Enter the habit type ([m]easurable, [c]heck): ").lower()

    # set the habit type
    if habit_type == "m":
        habit_type = "measurable"
    elif habit_type == "c":
        habit_type = "check"
    else:
        print("Please enter a valid habit type!")
        return habits

    # default value by type
    default_value = 0.0 if habit_type == "measurable" else False

    # update habits
    habits[habit_name] = {"type": habit_type, "log": {today: default_value}}

    return habits


today = datetime.now().strftime("%Y-%m-%d")
