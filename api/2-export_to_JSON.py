#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Exports data in the JSON format.
"""
import json
import requests
from sys import argv

try:
    user_id = int(argv[1])
except IndexError:
    print("You must enter an integer")
    exit()

response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
user_info = response.json()

response1 = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id))
user_tasks = response1.json()

completed_tasks = 0
total_tasks = 0
for task in user_tasks:
    if task['completed'] is True:
        completed_tasks += 1
    total_tasks += 1

print("Employee {} is done with tasks({}/{}):"
      .format(user_info['name'], completed_tasks, total_tasks))

task_title = [todos['title'] for todos in user_tasks
              if todos['completed'] is True]
for title in task_title:
    print("\t {}".format(title))

file = '{}.json'.format(user_id)

todo_dict = {user_id: []}
for task in user_tasks:
    todo_dict[user_id].append({"task": task['title'],
                               "completed": task['completed'],
                               "username": user_info['username']})

with open(file, 'w') as f:
    json.dump(todo_dict, f)
