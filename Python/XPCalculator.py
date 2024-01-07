def calculate_progress(current_xp, goal_xp):
    xp_per_exercise = 250  # Fixed XP gained per exercise
    needed_xp = goal_xp - current_xp
    if needed_xp <= 0:
        return "You have already reached or exceeded your goal!"

    exercises_needed = needed_xp // xp_per_exercise
    if needed_xp % xp_per_exercise != 0:
        exercises_needed += 1

    time_per_exercise = 2.5  # in minutes
    total_time_needed = exercises_needed * time_per_exercise

    hours = int(total_time_needed // 60)
    minutes = int(total_time_needed % 60)

    return needed_xp, exercises_needed, hours, minutes

def main():
    try:
        current_xp = int(input("Enter your current XP: "))
        goal_xp = int(input("Enter your goal XP: "))

        needed_xp, exercises_needed, hours, minutes = calculate_progress(current_xp, goal_xp)

        print(f"\nYou need {needed_xp} more XP to reach your goal.")
        print(f"You need to complete {exercises_needed} more exercises.")
        print(f"Estimated time to reach your goal: {hours} hours and {minutes} minutes.")
    except ValueError:
        print("Please enter valid numbers for XP.")
    print("Go grind hard Kise.")

if __name__ == "__main__":
    main()

