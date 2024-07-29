#!/usr/bin/python3
"""A python script that returns information about an
employees TODO list progress.
"""
import json
import requests
import sys


def get_todo_info():
    """A function that gets the todo information for a particular user id"""
    user_id = sys.argv[1]
    # GET /user/<id> resource for user info
    r = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                     .format(user_id))
    user = json.loads(r.text)
    user_name = user[0].get('name')

    # GET /user/<id>/todos for todo info
    r = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(user_id))
    todos = json.loads(r.text)
    comp_tasks = 0
    comp_titles = []
    total_tasks = 0
    for task in todos:
        total_tasks += 1
        if task['completed'] is True:
            comp_tasks += 1
            comp_titles.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, comp_tasks, total_tasks))
    for title in comp_titles:
        print("\t {}".format(title))


if __name__ == "__main__":
    get_todo_info()