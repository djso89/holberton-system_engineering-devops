#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    site = 'https://www.reddit.com/r/{}/hot.json?=10'.format(subreddit)
    req = requests.get(site, headers={'User-agent':'Kuppa'}).json()
    if 'message' in req and req['message'] == 'Not Found:':
        print("None")
        return
    for i in req['data']['children']:
        print(i['data']['title'])
