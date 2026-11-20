"""A small JSON-backed command-line task tracker."""
import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks(path=DATA_FILE):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks, path=DATA_FILE):
    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(title, path=DATA_FILE):
    tasks = load_tasks(path)
    task_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({"id": task_id, "title": title, "done": False})
    save_tasks(tasks, path)
    return task_id


def complete_task(task_id, path=DATA_FILE):
    tasks = load_tasks(path)
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks, path)
            return True
    return False


def format_tasks(tasks):
    if not tasks:
        return "No tasks yet."
    return "\n".join(
        f'{task["id"]}. [{"x" if task["done"] else " "}] {task["title"]}'
        for task in tasks
    )


def main():
    parser = argparse.ArgumentParser(description="A simple task tracker.")
    commands = parser.add_subparsers(dest="command", required=True)
    add_parser = commands.add_parser("add", help="Add a task")
    add_parser.add_argument("title")
    commands.add_parser("list", help="List tasks")
    done_parser = commands.add_parser("done", help="Complete a task")
    done_parser.add_argument("task_id", type=int)
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
