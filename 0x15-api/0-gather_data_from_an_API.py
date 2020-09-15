#!/usr/bin/python3
"""
script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    usr_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/"
        .format(argv[1]))

    name = usr_json.json().get("name")

    tasks_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(argv[1])).json()

    tasks_done = []

    for i in range(0, len(tasks_json)):
        if (tasks_json[i].get("completed")) is True:
            tasks_done.append(tasks_json[i].get("title"))

    print("Employee EMPLOYEE_NAME is done with tasks({}/{}):".
          format(name, len(tasks_done), len(tasks_json)))

    for i in range(0, len(tasks_done)):
        print("\t", tasks_done[i])
