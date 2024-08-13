#!/usr/bin/python3
"""This function queries the reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    """This function finds the titles of the first 10 hot
    posts listed for a given subreddit."""
    redd_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(redd_url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])

        else:
            print(None)
    except requests.RequestException:
        print(None)
