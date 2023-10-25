import random

#A script that i wrote to help my friend to write his script scheduals"
shifts = {
    "morning": (7, 15),
    "afternoon": (15, 23),
    "night": (23, 7)
}

# List of workers
workers = ["shaked", "ron", "shlomi", "vlad", "doron"]

# Initialize the schedule dictionary
schedule = {worker: {day: [] for day in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]}
            for worker in workers}

# Mapping of options to shifts
option_to_shifts = {
    "a": ["morning"],
    "b": ["afternoon"],
    "c": ["night"],
    "a+b": ["morning", "afternoon"],
    "b+c": ["afternoon", "night"],
    "a+c": ["morning", "night"],
    "a+b+c": ["morning", "afternoon", "night"]
}

# Input each worker's availability
for day in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
    print(f"\nEnter availability for {day.capitalize()}:")
    for worker in workers:
        while True:
            availability_input = input(
                f"{worker.capitalize()}'s Availability (a, b, c, a+b, b+c, a+c, a+b+c, x: None): ").lower()
            if availability_input == "":
                print("Please enter a valid option.")
            elif availability_input == "x":
                selected_shifts = []
                break
            else:
                selected_shifts = []
                options = availability_input.split('+')
                valid_options = True
                for option in options:
                    if option not in option_to_shifts:
                        print(f"Invalid option: {option}")
                        valid_options = False
                        break
                    selected_shifts.extend(option_to_shifts[option])
                if valid_options:
                    # Ensure the same worker doesn't work consecutive shifts
                    if "morning" in selected_shifts and "afternoon" in selected_shifts:
                        selected_shifts.remove("afternoon")
                    if "afternoon" in selected_shifts and "night" in selected_shifts:
                        selected_shifts.remove("night")
                    if "night" in selected_shifts and "morning" in selected_shifts:
                        selected_shifts.remove("morning")
                    break
        schedule[worker][day] = selected_shifts

# Generate the work schedule
print("\nGenerated Work Schedule:\n")

# Generate and print schedule for each day
header = ["Day", "Morning", "Afternoon", "Night"]
data = []
for day in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
    assigned_workers = {"morning": None, "afternoon": None, "night": None}
    for shift in ["morning", "afternoon", "night"]:
        available_workers = [worker for worker in workers if shift in schedule[worker][day]]

        # Ensure the same worker doesn't work consecutive shifts
        if assigned_workers[shift]:
            available_workers = [worker for worker in available_workers if worker != assigned_workers[shift]]

        if available_workers:
            random_worker = random.choice(available_workers)
            assigned_workers[shift] = random_worker
        else:
            assigned_workers[shift] = "Empty"

    data.append([day.capitalize(), assigned_workers["morning"].capitalize(), assigned_workers["afternoon"].capitalize(),
                 assigned_workers["night"].capitalize()])

# Print the schedule in a table
print("\n+------------+------------+------------+----------+")
print("| Day        | Morning    | Afternoon  | Night      |")
print("+------------+------------+------------+------------+")
for row in data:
    print("| {:<10} | {:<10} | {:<10} | {:<10} |".format(*row))
print("+------------+------------+------------+------------+")

