#!/usr/bin/python3
"""
A python script that gathers employee data from an API and exports it to a CSV file.
"""
import re
import requests
import sys
import csv

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            user_id = int(sys.argv[1])
            user = requests.get('{}/users/{}'.format(REST_API, user_id)).json()
            todos = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = user.get('name')
            username = user.get('username')
            tasks = list(filter(lambda x: x.get('userId') == user_id, todos))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            
            # Print employee's completed tasks
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
            
            # Write tasks to CSV file
            csv_filename = '{}.csv'.format(user_id)
            with open(csv_filename, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for task in tasks:
                    csvwriter.writerow([user_id, username, task.get('completed'), task.get('title')])
            
            print(f"Data exported to {csv_filename} successfully.")
