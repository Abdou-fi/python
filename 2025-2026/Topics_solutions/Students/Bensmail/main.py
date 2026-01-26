
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    num = int(input("Enter task number to remove: "))
                    removed = tasks.pop(num - 1)
                    print(f"Removed: {removed}")
                except (ValueError, IndexError):
                    print("Invalid number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
