import requests, bs4


url="https://autbor.com/example3.html"

response = requests.get(url, timeout=5)
response.raise_for_status()

# creating a bs4 object 
example_soup = bs4.BeautifulSoup(response.text, "html.parser")

# print(type(example_soup))
# print(example_soup) ill see the html body


# you can load html from a file

with open("/home/kit/Kitstdios/learning-python/beatifulsoup/index.html") as file:
    another_soup = bs4.BeautifulSoup(file,"html.parser")

#print(another_soup)

# once you have the beautiful soup object you can use the methods to find specific things

# lets look at the title of the page
print(type(example_soup.title), another_soup.title)
