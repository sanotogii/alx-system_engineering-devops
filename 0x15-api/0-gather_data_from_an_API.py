#!/usr/bin/python3

"""
 Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    _id = int(sys.argv[1])
    done = 0
    total = 0
    title = []

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = response.json()
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    user_response = requests.get(user_url)
    user_json = user_response.json()
    employee = user_json.get('name', None)

    for item in data:
        if item.get('userId', None) == _id:
            if item.get('completed') is True:
                done += 1
                title.append(item.get("title", None))
            total += 1

    print('Employee {} is done with tasks({}/{}):'.format(employee, done,
                                                          total))
    for i in title:
        print('\t {}'.format(i))
