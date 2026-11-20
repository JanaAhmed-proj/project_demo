"""A small JSON-backed command-line task tracker."""

import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks(path=DATA_FILE):
    """Load tasks from JSON, returning an empty list if no file exists yet."""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks, path=DATA_FILE):
    """Save tasks to a JSON file."""
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(title, path=DATA_FILE):
    """Add a task and return its assigned ID."""
    tasks = load_tasks(path)
    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({"id": next_id, "title": title, "done": False})
    save_tasks(tasks, path)
    return next_id


def complete_task(task_id, path=DATA_FILE):
    """Mark a task as complete. Return True if it was found."""
    tasks = load_tasks(path)
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks, path)
            return True
    return False


def format_tasks(tasks):
    """Return a readable representation of the task list."""
    if not tasks:
        return "No tasks yet."

    lines = []
    for task in tasks:
        status = "x" if task["done"] else " "
        lines.append(f'{task["id"]}. [{status}] {task["title"]}')
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="A simple command-line task tracker.")
    commands = parser.add_subparsers(dest="command", required=True)

    add_parser = commands.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task description")

    commands.add_parser("list", help="List all tasks")

    done_parser = commands.add_parser("done", help="Mark a task as complete")
    done_parser.add_argument("task_id", type=int, help="ID of the task")

    args = parser.parse_args()

    if args.command == "add":
        task_id = add_task(args.title)
        print(f"Added task {task_id}: {args.title}")
    elif args.command == "list":
        print(format_tasks(load_tasks()))
    elif args.command == "done":
        if complete_task(args.task_id):
            print(f"Task {args.task_id} marked as complete.")
        else:
            print(f"Task {args.task_id} was not found.")


if __name__ == "__main__":
    main()
