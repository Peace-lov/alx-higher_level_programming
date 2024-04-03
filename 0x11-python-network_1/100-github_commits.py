#!/usr/bin/python3
""" The 10 most recent commits on a given github repo
Usage: ./100-github_commits.py <repo. name> repo owner>
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for a in range(10):
            print("{}: {}".format(
                commits[a].get("sha"),
                commits[a].get("commit").get("author").get("name")))
    except IndexError:
        pass
