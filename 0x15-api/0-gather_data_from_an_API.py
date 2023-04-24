#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseURL = "https://jsonplaceholder.typicode.com/users"
    url = baseURL + "/" + employeeId
    response = requests.get(url)
    employeeName = response.json().get("name")
    todoURL = url + "/todos"
    response = requests.get(todoURL)
    tasks = response.json()
    done = 0
    doneTask = []

    for task in tasks:
        if task.get('completed'):
            doneTask.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employeeName,
        done,
        len(tasks)
        )
    )

    for task in doneTask:
        print("\t {}".format(task.get('title')))
