import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "completed": False})
    print("✅ Task added!")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("🎉 Task marked as complete!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"🗑️ Deleted: {deleted['title']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n📝 To-Do List Menu")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("📦 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
