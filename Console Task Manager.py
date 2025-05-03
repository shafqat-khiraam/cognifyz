class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"📋 Title: {self.title}\n📝 Description: {self.description}\n✅ Status: {self.status}"

tasks = []

def create_task():
    print("\n--- Let's add a new task! ---")
    title = input("What’s the task title? ")
    description = input("Can you describe the task? ")
    task = Task(title, description)
    tasks.append(task)
    print("\n✨ Task added successfully!")

def read_tasks():
    print("\n--- Here are your tasks ---")
    if not tasks:
        print("You have no tasks at the moment. Time to get productive!")
    else:
        for i, task in enumerate(tasks):
            print(f"\nTask {i+1}:\n{task}")

def update_task():
    read_tasks()
    if not tasks:
        return  # Exit if there are no tasks to update
    task_num = int(input("\nWhich task number would you like to update? ")) - 1
    if 0 <= task_num < len(tasks):
        print("\n--- Update task details ---")
        title = input("New title (leave blank to keep current): ") or tasks[task_num].title
        description = input("New description (leave blank to keep current): ") or tasks[task_num].description
        status = input("New status (Complete/Incomplete, leave blank to keep current): ") or tasks[task_num].status
        tasks[task_num].title = title
        tasks[task_num].description = description
        tasks[task_num].status = status
        print("\n✅ Task updated successfully!")
    else:
        print("Oops! That task number doesn’t exist.")

def delete_task():
    read_tasks()
    if not tasks:
        return  # Exit if there are no tasks to delete
    task_num = int(input("\nWhich task number would you like to delete? ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("\n🗑️ Task deleted successfully!")
    else:
        print("Hmm, that task number isn’t valid.")

def menu():
    print("👋 Welcome to your Task Manager!\n")
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a Task\n2. View All Tasks\n3. Update a Task\n4. Delete a Task\n5. Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nGoodbye! 👋 Keep crushing those tasks!")
            break  # Exit the loop
        else:
            print("\nThat’s not a valid option. Try again!")

if __name__ == "__main__":
    menu()
