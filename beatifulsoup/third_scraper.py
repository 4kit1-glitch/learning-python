import requests
import bs4

from pathlib import Path
from strore_req import save_webcontent


# lets do some scaping challenges with 

webhtml = Path.cwd() / "quotestoscrape.html"


with webhtml.open("r", encoding="utf-8") as web_handle:
    soup = bs4.BeautifulSoup(web_handle, "html.parser")


# selecting the qoute + the author of the first qoute

found = soup.select_one("div.quote span.text") 

quote = found.text if found else "No qoute"


found = soup.select_one("div.quote small.author")

author = found.text if found else "No author"

print(quote, "by", author)