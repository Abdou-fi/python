

# This list will store all tasks
tasks = []

# Keep the program running
while True:


    # Show menu to the user

    print("1 Add a task")
    print("2 View tasks")
    print("3 Delete a task")
    print("4 Exit")

    # Ask user to choose an option
    choice = input("Choose an option (1-4): ")

    # OPTION 1: Add a task
    if choice == "1":
        task = input("Enter your task: ")  # User writes a task
        tasks.append(task)                 # Add task to the list
        print("Task added.")

    # OPTION 2: View tasks
    elif choice == "2":
        if len(tasks) == 0:                # Check if list is empty
            print("No tasks found.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):    # Loop through tasks
                print(i + 1, "-", tasks[i])

    # OPTION 3: Delete a task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

            number = int(input("Enter task number to delete: "))
            tasks.pop(number - 1)           # Remove the task
            print("Task deleted.")

    # OPTION 4: Exit program
    elif choice == "4":
        print("Program ended.")
        break                               # Stop the loop

    # If user enters wrong option
    else:
        print(" enter number from 1 to 4 ")

