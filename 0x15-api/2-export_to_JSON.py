#!/usr/bin/python3
"""  script to export data in the CSV format."""

import json
import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/".format(argv[1]))

    tasks_json = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(argv[1])).json()

    usr_info_dict = {}
    usr_info_dict["{}".format(argv[1])] = []
    for x in tasks_json:
        usr_info_dict["{}".format(argv[1])].append({
            'task': x.get("title"),
            'completed': x.get('completed'),
            'username': user_json.json().get("username")
        })

    with open("{}.csv".format(argv[1]), 'w') as file:
        json.dump(usr_info_dict, file)
