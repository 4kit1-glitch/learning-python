import requests
import bs4

from pathlib import Path

url = Path.cwd() / "example3.html"


with url.open("r", encoding="utf-8") as site:
    my_soup = bs4.BeautifulSoup(site, "html.parser")


# learning css selectors patterns

# find by tag name just use the .select then within we have the tag

print(my_soup.select("a")) # a list of all the hyperlinks in the html


# find by class (how developers lable things )
# there are two ways of doing it lets say general and sepecific

# generally  -- find all elements with class slogan

print(my_soup.select(".slogan"))


# specific -- find all h tags with the class slogan
print(my_soup.select("h1.aclass"))