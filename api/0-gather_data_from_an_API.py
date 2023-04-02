#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


user_id = int(argv[1])

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
