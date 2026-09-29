import requests

"""
opens a website to that exact page and sends a response 
the 
"""
try:
    response = requests.get("https://automatetheboringstuff.com/files/rj.txt", timeout=5)
    print(response.text[:210])
except (requests.ConnectionError, requests.ConnectTimeout) as e:
    print(f"request failed: {e}")

