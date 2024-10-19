## Task Manager project for Python Basics course ##

import json
import hashlib

# ----- SECTION 1: User Registration and Login ----- #

# File to store user data #
USERS_FILE = 'users.json'

# Load users from the file #
def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save users to the file #
def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file)

# Hash the password using SHA-256 #
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register a new user #
def register_user(username, password):
    users = load_users()

    if username in users:
        return "Username already exists. Please choose another one."

    users[username] = {
        'password': hash_password(password)
    }
    save_users(users)
    return "User registered successfully!"

# Login user #
def login_user(username, password):
    users = load_users()

    if username not in users:
        return "User not found."

    hashed_password = hash_password(password)

    if users[username]['password'] == hashed_password:
        return "Login successful!"
    else:
        return "Incorrect password."

## ----- SECTION 2: Task Management ----- ##

# File to store task data #
TASKS_FILE = 'tasks.json'

# Load tasks from the file #
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save tasks to the file #
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Create a task for a user #
def create_task(username, task_name):
    tasks = load_tasks()
    if username not in tasks:
        tasks[username] = []

    tasks[username].append({
        'name': task_name,
        'completed': False
    })

    save_tasks(tasks)
    return "Task added successfully."

# View all tasks for a user (with index) #
def view_tasks(username):
    tasks = load_tasks()
    user_tasks = tasks.get(username, [])
    if not user_tasks:
        return "No tasks found."
    
    task_list = []
    for i, task in enumerate(user_tasks, 1):  # Index starting from 1
        status = "Completed" if task['completed'] else "Pending"
        task_list.append(f"{i}. Task: {task['name']} | Status: {status}")
    return "\n".join(task_list)

# Mark a task as completed by index #
def mark_task_complete(username, task_index):
    tasks = load_tasks()

    if username in tasks:
        if 0 <= task_index < len(tasks[username]):
            tasks[username][task_index]['completed'] = True
            save_tasks(tasks)
            return "Task marked as complete."
        else:
            return "Invalid task index."
    
    return "No tasks found."

# Delete a task by index #
def delete_task(username, task_index):
    tasks = load_tasks()

    if username in tasks:
        if 0 <= task_index < len(tasks[username]):
            del tasks[username][task_index]
            save_tasks(tasks)
            return "Task deleted."
        else:
            return "Invalid task index."
    
    return "No tasks found."

## ----- SECTION 3: User Interaction ----- ##

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Select option (1, 2, or 3): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(register_user(username, password))

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_result = login_user(username, password)
            print(login_result)

            if login_result == "Login successful!":
                task_manager(username)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

## ----- SECTION 4: Task Manager After Login ----- ##

def task_manager(username):
    while True:
        print(f"\n--- Task Manager for {username} ---")
        print("1. Create a task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Delete a task")
        print("5. Log out")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            print(create_task(username, task_name))

        elif choice == '2':
            print(view_tasks(username))

        elif choice == '3':
            task_index = int(input("Enter task index to mark as complete: ")) - 1  # Convert to zero-based index
            print(mark_task_complete(username, task_index))

        elif choice == '4':
            task_index = int(input("Enter task index to delete: ")) - 1  # Convert to zero-based index
            print(delete_task(username, task_index))

        elif choice == '5':
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

# ----- Run the Program -----#
if __name__ == '__main__':
    main()
