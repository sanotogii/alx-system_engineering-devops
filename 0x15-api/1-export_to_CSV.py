#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports data in CSV format.
"""

import requests
import sys
import csv

if __name__ == '__main__':
    _id = int(sys.argv[1])
    done = 0
    total = 0
    title = []
    tasks = []

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    user_response = requests.get(user_url)
    user_json = user_response.json()
    employee = user_json.get('username', None)

    for item in data:
        if item.get('userId', None) == _id:
            task_completed = item.get('completed')
            task_title = item.get("title", None)
            tasks.append((item.get('userId', None), employee, task_completed, task_title))
            if task_completed:
                done += 1
                title.append(task_title)
            total += 1

    csv_filename = '{}.csv'.format(_id)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(task)

