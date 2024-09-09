""" Adding suport to en and pt_BR """

import requests


def hello():
    """simple function to return a string"""
    c = requests.get(
        "https://api.github.com/repos/insper/dev-aberto/commits", timeout=10
    )
    info = c.json()
    commit_info = info[0]["commit"]["author"]
    return commit_info["date"], commit_info["name"]
