# To-Do List Manager: A command-line application that allows users to add, view, and delete tasks, 
# potentially saving the data to a simple text file.

def display_menu():
    print("To-Do List Manager")
    print("-------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")   
    if not tasks:
        print("No tasks available.")
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully.")

def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return
    view_tasks(tasks)
    task_index = int(input("Enter the task number to delete: "))
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number.")
    else:
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' deleted successfully.")   
        
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Exiting the To-Do List Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
# This is a simple implementation of a To-Do List Manager. It allows users to view, add, and delete tasks. The tasks are stored in a list in memory, and the program runs in a loop until the user chooses to exit.
# Note: This implementation does not save tasks to a file. To add file persistence, you could implement file read/write operations.
