
#function that displays the main menu
def display_menu():
    print("\n Welcome to the to-do list app!")
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")

#function that adds tasks to to-do list
def add_task(tasks):
    task_title = input("Please enter the task description: ").strip()
    if task_title:
        tasks.append({"title": task_title, "status": "Incomplete"})
        print("Task added successfully!")
    else:
        print("Task description cannot be empty. Please try again.")

#function for viewing all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available to show.")
        return
    print("\nTasks: ")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} {[task['status']]}")

#function for masking task as complete
def task_completed(tasks):
    if not tasks:
        print("No tasks to mark as complete.")
        return
    
    # show tasks with index
    view_tasks(tasks)
    try: 
        index = int(input("Please enter task index to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Complete"
            print(f"Task '{tasks[index]['title']}' has been marked as 'Complete'.")
        else: 
            print("Invalid task index. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#function to delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
        return
    view_tasks(tasks)
    try:
        index = int(input("Please enter task index to be deleted: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task['title']}' has been deleted.")
        else: 
            print("Invalid task index. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


#empty list to store tasks
tasks = []  

while True:
    display_menu()
    choice = input("Please enter your selection: ")
    
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        task_completed(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Exiting the menu")
        break
    else:
        print("Invalid choice. Please select a valid option.")