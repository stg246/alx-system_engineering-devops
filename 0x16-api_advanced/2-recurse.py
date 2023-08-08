#!/usr/bin/python3
# Defines recurse function

import requests as r


def recurse(subreddit, hot_list=[], last=None):
    """
    queries the Reddit API for the titles of all a subreddit's hot articles

    return: List of the titles, or None if none
    """
    g = r.get('https://api.reddit.com/r/{}/hot'
              .format(subreddit), headers={
                  'user-agent': 'python:v3.5.2 (by /u/maxastuart)'},
              params={'limit': 1, 'after': last})
    if g.status_code is 200 and g.json().get('data') is not None:
        p = g.json().get('data').get('children')
        if len(p) > 0:
            t = p[0].get('data').get('title')
            if g.json().get('data').get('after'):
                return [t] + (recurse(subreddit, hot_list,
                                      g.json().get('data').get('after')))
            else:
                return []
        else:
            return []
    else:
        return None
