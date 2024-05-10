#!/usr/bin/python3
<<<<<<< HEAD
"""
list 10 commits (from the most recent to oldest) of the repository
"rails" by the user "rails"
You must use the GitHub API
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


def get_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.json())
        return

    commits = response.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py repository_name owner_name")
    else:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        get_commits(repo_name, owner_name)
=======
"""Takes 2 arguments in order to solve this challenge"""
import sys
import requests
if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
>>>>>>> 85c830d5152b4c87b4bb23ab8ef9119fffe1b20d
