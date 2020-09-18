#!/usr/bin/python3
"""
returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    req = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={
            'User-agent': 'Mozilla 80.0.1'
        }).json()
    return (0 if ('message' in req and req['message'] == 'Not Found')
            else req['data']['subscribers'])
