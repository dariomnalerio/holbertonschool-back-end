#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Exports data in the JSON format.
"""
import json
import requests

todo_url = "https://jsonplaceholder.typicode.com/todos?userId="
response = requests.get("https://jsonplaceholder.typicode.com/users/")
users_info = response.json()

todo_dict = {}

for user in users_info:
    user_id = user['id']
    response = requests.get(todo_url + '{}'
                            .format(user_id))
    user_tasks = response.json()

    todo_dict[user_id] = []
    for task in user_tasks:
        todo_dict[user_id].append({"task": task['title'],
                                   "completed": task['completed'],
                                   "username": user['username']})

with open('todo_all_employees.json', 'w') as f:
    json.dump(todo_dict, f)
