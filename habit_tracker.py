import json


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


def view_all_habits(habits):
    """list all habits"""
    for habit in habits:
        print(f"{habit}: {habits[habit]['done']}")


def add_new_habit(habits):
    """add new habit to habits, return updated habits"""
    habit_name = input("Enter the habit name: ")
    # if the habit already exists, don't update habits
    if habit_name in habits:
        print("This habit already exists!")
        return habits
    # add the new habit
    habits[habit_name] = {"done": False}
    return habits


def mark_habit_as_done(habits):
    """update 'done' to True"""
    habit_name = input("Enter the habit name: ")

    # if the habit doesn't exist, don't change habits
    if habit_name not in habits:
        print("Habit doesn't exist")
        return habits

    # update the habit
    habits[habit_name]["done"] = True
    return habits


# load the habits from habits.json
habits = load_habits()

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
        habits = add_new_habit(habits)
        save_habits(habits)
    elif user_input == "3":
        habits = mark_habit_as_done(habits)
        save_habits(habits)
