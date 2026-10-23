import bs4
import requests

from pathlib import Path


webhtml = Path.cwd() / "quotestoscrape.html"


with webhtml.open("r", encoding="utf-8") as web_handle:
    soup = bs4.BeautifulSoup(web_handle, "html.parser")


# 

found = soup.select_one("div.row li.next a")

print(found["href"]) if found else print("next link not found")