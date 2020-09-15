#!/usr/bin/python3
"""
export data in the JSON format
"""

import json
import requests

if __name__ == '__main__':
    users_dict = requests.get(
        "https://jsonplaceholder.typicode.com/users/").json()
    users = 0
    for i in users_dict:
        users = users + 1
    full_dict = {}
    for user in range(1, users + 1):
        user_info = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/"
            .format(user))
        name = user_info.json().get("username")
        user_todo = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos"
            .format(user)).json()
        full_dict["{}".format(user)] = []
        for tasks in range(0, len(user_todo)):
            full_dict["{}".format(user)].append({
                "username": name,
                "task": user_todo[tasks].get("title"),
                "completed": user_todo[tasks].get("completed")
            })
    with open("todo_all_employees.json", 'w') as file_o:
        json.dump(full_dict, file_o)
