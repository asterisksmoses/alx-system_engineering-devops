#!/usr/bin/python3
"""This script is recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit."""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """This is a recursive function that returns a list containing 
    the titles of all hot articles for a given subreddit."""
    redd_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    parameters = {
            "after": after,
            "count": count,
            "limit": 100
        }
    response = requests.get(redd_url, headers=headers, params=parameters, allow_redirects=False)
    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for x in results.get("children"):
        hot_list.append(x.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
