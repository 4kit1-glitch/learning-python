import bs4, requests
from pathlib import Path



webhtml = Path.cwd() / "quotestoscrape.html"


with webhtml.open("r", encoding="utf-8") as web_handle:
    soup = bs4.BeautifulSoup(web_handle, "html.parser")

# extracting the link to the abt page of the first author
found = soup.select_one("div.quote a")  # selects the link tag

print(found["href"]) if found else print("no link found")


# this demonstrates that class attributes give a list -- AttributeValueList
found = soup.select_one("div.quote span")
print(type(found["class"])) if found else print("no link found")