#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)
    
    employee_name = user_response.json().get('name')

    # Get TODO list
    todo_url = f"{base_url}/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    tasks = todo_response.json()

    # Calculate the number of done tasks and total tasks
    done_tasks = [task for task in tasks if task.get('completed')]
    total_tasks = len(tasks)
    done_count = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_count, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
