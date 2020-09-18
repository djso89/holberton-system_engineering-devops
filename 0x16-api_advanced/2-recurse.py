#!/usr/bin/python3
"""
queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], last=""):
    site = 'https://www.reddit.com/r/{}/hot.json?limit=100'\
               .format(subreddit) +\
               ('&after={}'.format(last) if last != "" else "")
    req = requests.get(site, headers={'User-agent': 'Mozilla 80.0'}).json()
    if 'message' in req and req['message'] == 'Not Found':
        return None

    hot_arr = req['data']['children']

    if len(hot_arr) == 0:
        return hot_list
    hot_list.extend(hot_arr[i]["data"]["title"]
                    for i in range(0, len(hot_arr)))
    return (recurse(subreddit, hot_list, hot_arr[-1]["data"]["name"]))
