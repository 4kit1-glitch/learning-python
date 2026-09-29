import requests

# lets open a bad website and see what hppens

try:
    response = requests.get("https://www.notawebsite.com", timeout=5)
    print(response.text)
except requests.exceptions.ConnectionError:
    print("failed to connect to website")


# opening a website where we need success to occur use request_for_status()
# it gives us a status with a correct error code