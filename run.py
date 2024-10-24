
# Main program that runs when user accesses the server
def marvin_task_prompt():
    print('''Okay! Now that all that's out of the way. Do you have something, Anything for me to work on
    other than Vogon Poetry? ANYTHING?! ... (entire message)''')
    task = input("Please insert task: ")
    
    # Task saving logic
    with open("task_submissions.txt", "a") as task_file:
        task_file.write(f"{task}\n")
    
    print(f"Your task '{task}' has been saved for analysis.")

if __name__ == "__main__":
    marvin_task_prompt()
