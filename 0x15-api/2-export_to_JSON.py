#!/usr/bin/python3

"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
exports data in JSON format.
"""
import json
import requests
import sys


if __name__ == '__main__':
    _id = int(sys.argv[1])
    tasks = []

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    user_response = requests.get(user_url)
    user_json = user_response.json()
    employe = user_json.get('username', None)

    for item in data:
        if item.get('userId', None) == _id:
            task = {
                "task": item.get("title", None),
                "completed": item.get("completed"),
                "username": employe
            }
            tasks.append(task)

    json_data = {str(_id): tasks}

    json_filename = '{}.json'.format(_id)
    with open(json_filename, mode='w') as file:
        json.dump(json_data, file)
