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



