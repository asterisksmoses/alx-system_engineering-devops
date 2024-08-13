#!/usr/bin/python3
"""This script queries the reddit API and returns the number of subscribers 
for a given subreddit."""

import requests

def number_of_subscribers(subreddit):
    """This function finds the number of subscribers in a
    particular subreddit."""
    redd_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        resp = requests.get(redd_url, headers=headers, allow_redirects=False)
        if resp.status_code == 200:
            data = resp.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
