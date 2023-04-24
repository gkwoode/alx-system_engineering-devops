#!/usr/bin/python3
"""
Using what you did in the task #0, extend your 
    - Python script to export data in the CSV format
"""

import requests
import sys
import csv

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseURL = "https://jsonplaceholder.typicode.com/users"
    url = baseURL + "/" + employeeId
    response = requests.get(url)
    username = response.json().get("username")
    todoURL = url + "/todos"
    response = requests.get(todoURL)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                employeeId, 
                username, 
                task.get('completed'),
                task.get('title')
                )
            )
