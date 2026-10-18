import requests, bs4


url="https://autbor.com/example3.html"

response = requests.get(url, timeout=5)
response.raise_for_status()

# creating a bs4 object 
example_soup = bs4.BeautifulSoup(response.text, "html.parser")

print(type(example_soup))
# print(example_soup) ill see the html body