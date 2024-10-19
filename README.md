<img width="851" alt="image" src="https://github.com/user-attachments/assets/310dfb52-5a9c-46a7-ba1b-223f5fe23958">

# task_mgr_with_user_reg
Task Manager with User Registration and Login

# Problem Statement: #

In today’s world, individuals often need to keep track of various tasks in a structured way. You are tasked with building a Task Manager that allows users to manage their tasks. The system should include user authentication, meaning each user has to log in with a username and password. Once logged in, users can create, view, update, and delete their tasks. Each user’s tasks should be stored separately, and only the authenticated user can access their tasks.

# Objectives: #
1. Design and implement a user authentication system (login and registration)
2. Create a task management system that allows users to:
 Add, view, mark as completed, and delete tasks
3. Use file handling to store user credentials and tasks persistently
4. Create an interactive menu-driven interface to manage tasks

# Steps to Perform: #
## 1. User Authentication: ##
**Registration:**
1. Create a function to prompt the user to enter a username and password
2. Ensure that the username is unique, and hash the password for security before storing it in a file

**Login:**
1. Create a function to prompt the user for their username and password, validate the credentials by comparing them with the stored data, and grant access to the task manager upon successful login

## 2. Add a Task:##
1. Create a function that prompts the user for a task description. Assign a unique task ID and set the status to Pending
2. Store the task in a file, and confirm that the task was added

## 3. View Tasks:##
1. Create a function to retrieve and display all tasks for the logged-in user
2. Each task should show the task ID, description, and status (Pending or Completed)

## 4. Mark a Task as Completed:##
1. Create a function that allows the user to select a task by its ID and update its status to Completed

## 5. Delete a Task: ##
1. Create a function that allows the user to select a task by its ID and delete it from their task list
