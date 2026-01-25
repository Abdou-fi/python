#!/usr/bin/env python3
"""
To-Do List Manager (CLI)
- Saves tasks to tasks.json
- Add / list / mark done / delete / search
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


DATA_FILE = "tasks.json"


def now_iso() -> str:
    """Return current time in ISO format (readable + sortable)."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_tasks(path: str = DATA_FILE) -> List[Dict]:
    """Load tasks from a JSON file. If file doesn't exist, return empty list."""
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            # Basic safety check: ensure expected keys exist
            cleaned = []
            for t in data:
                if isinstance(t, dict) and "id" in t and "title" in t:
                    t.setdefault("done", False)
                    t.setdefault("created_at", "")
                    cleaned.append(t)
            return cleaned
        return []
    except (json.JSONDecodeError, OSError):
        # If file is corrupted or unreadable, start fresh
        return []


def save_tasks(tasks: List[Dict], path: str = DATA_FILE) -> None:
    """Save tasks to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def next_id(tasks: List[Dict]) -> int:
    """Generate the next task id (max existing id + 1)."""
    if not tasks:
        return 1
    return max(int(t.get("id", 0)) for t in tasks) + 1


def print_task(task: Dict) -> None:
    """Print a single task nicely."""
    status = "✅" if task.get("done") else "⬜"
    tid = task.get("id")
    title = task.get("title", "").strip()
    created = task.get("created_at", "")
    if created:
        print(f"{status} [{tid}] {title}  (created: {created})")
    else:
        print(f"{status} [{tid}] {title}")


def list_tasks(tasks: List[Dict], mode: str = "all") -> None:
    """
    mode: 'all' | 'pending' | 'done'
    """
    if mode not in {"all", "pending", "done"}:
        mode = "all"

    filtered = []
    for t in tasks:
        done = bool(t.get("done"))
        if mode == "all":
            filtered.append(t)
        elif mode == "pending" and not done:
            filtered.append(t)
        elif mode == "done" and done:
            filtered.append(t)

    if not filtered:
        print("\n(No tasks to show.)\n")
        return

    print()
    for t in sorted(filtered, key=lambda x: int(x.get("id", 0))):
        print_task(t)
    print()


def find_task(tasks: List[Dict], task_id: int) -> Optional[Dict]:
    """Return a task dict by id, or None if not found."""
    for t in tasks:
        if int(t.get("id", -1)) == task_id:
            return t
    return None


def read_int(prompt: str) -> Optional[int]:
    """Read an integer from user input. Return None if invalid."""
    s = input(prompt).strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def add_task(tasks: List[Dict]) -> None:
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    t = {
        "id": next_id(tasks),
        "title": title,
        "done": False,
        "created_at": now_iso(),
    }
    tasks.append(t)
    print("Added:")
    print_task(t)


def toggle_done(tasks: List[Dict]) -> None:
    task_id = read_int("Enter task id to toggle done/undone: ")
    if task_id is None:
        print("Please enter a valid number.")
        return

    t = find_task(tasks, task_id)
    if not t:
        print(f"No task found with id {task_id}.")
        return

    t["done"] = not bool(t.get("done"))
    print("Updated:")
    print_task(t)


def delete_task(tasks: List[Dict]) -> None:
    task_id = read_int("Enter task id to delete: ")
    if task_id is None:
        print("Please enter a valid number.")
        return

    t = find_task(tasks, task_id)
    if not t:
        print(f"No task found with id {task_id}.")
        return

    tasks.remove(t)
    print(f"Deleted task [{task_id}].")


def search_tasks(tasks: List[Dict]) -> None:
    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
        print("Keyword cannot be empty.")
        return

    results = [t for t in tasks if keyword in t.get("title", "").lower()]
    if not results:
        print("No matching tasks found.")
        return

    print("\nSearch results:")
    for t in sorted(results, key=lambda x: int(x.get("id", 0))):
        print_task(t)
    print()


def menu() -> None:
    print("========== TO-DO LIST MANAGER ==========")
    print("1) Add task")
    print("2) List all tasks")
    print("3) List pending tasks")
    print("4) List done tasks")
    print("5) Toggle done/undone")
    print("6) Delete task")
    print("7) Search tasks")
    print("0) Save & Quit")
    print("=======================================")


def main() -> None:
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s) from {DATA_FILE}.\n")

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            list_tasks(tasks, "all")
        elif choice == "3":
            list_tasks(tasks, "pending")
        elif choice == "4":
            list_tasks(tasks, "done")
        elif choice == "5":
            toggle_done(tasks)
            save_tasks(tasks)
        elif choice == "6":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "7":
            search_tasks(tasks)
        elif choice == "0":
            save_tasks(tasks)
            print(f"Saved to {DATA_FILE}. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu.")

        print()  # spacing


if __name__ == "__main__":
    main()
