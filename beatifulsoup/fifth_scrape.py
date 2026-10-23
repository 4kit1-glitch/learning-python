import bs4, requests
from pathlib import Path


webhtml = Path.cwd() / "quotestoscrape.html"


with webhtml.open("r", encoding="utf-8") as web_handle:
    soup = bs4.BeautifulSoup(web_handle, "html.parser")


# find all the tags from the second qoute

quotes = soup.select("div.quote")

try:
    secondq = quotes[1]
    #inner_soup = bs4.BeautifulSoup(str(secondq), "html.parser")
    for tag in secondq.select("div.tags a.tag"):
        print(tag.text)
except (IndexError,TypeError) as err:
    print(f"error as {err}")
