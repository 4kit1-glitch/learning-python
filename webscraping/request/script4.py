import requests

# Grab a small image
response = requests.get("https://www.python.org/static/img/python-logo.png")

print("--- .text output (first 100 chars) ---")
print(response.text[:100])

print("\n--- .content output (first 100 bytes) ---")
print(response.content[:100])

print(f"\nContent-Type: {response.headers['Content-Type']}")