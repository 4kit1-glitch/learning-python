# github_api.py
import requests

BASE_URL = "https://api.github.com"

def get_user(username):
    response = requests.get(f"{BASE_URL}/users/{username}", timeout=10)
    response.raise_for_status()
    data = response.json()
    return {
        "login": data["login"],
        "followers": data["followers"],
        "repo_count": data["public_repos"],
    }