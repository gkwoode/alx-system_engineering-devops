#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
    - Python script to export data in the JSON format
"""

import json
import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseURL = "https://jsonplaceholder.typicode.com/users"
    url = baseURL + "/" + employeeId
    response = requests.get(url)
    username = response.json().get("username")
    todoURL = url + "/todos"
    response = requests.get(todoURL)
    tasks = response.json()

    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dictionary, filename)
