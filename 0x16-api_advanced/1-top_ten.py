#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    site = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    h = {'User-Agent': 'Mozilla 5.0'}
    req = requests.get(site, headers=h)

    if req.status_code == 404:
        print('None')
    else:
        data = req.json().get('data')
        posts = data.get('children')
        for i in posts:
            print(i.get('data').get('title'))
