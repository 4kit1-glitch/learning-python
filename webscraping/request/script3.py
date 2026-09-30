# downloading content to the harddrive
# always open the file to download to in wb or b or ab as binary, that way we can effectively send what ever we need


"""
to download and save content with request
1. call the request.get to the page and wait for response
2. open the file to store as bytes with the right extension
3. call the response.iter_content() and specify the iter size
4. and loop throught the iter chunks and write to the file 
"""
import requests
from pathlib import Path

CHUNK_SIZE = 8192 # 8 kb standard stream size
store_dir = Path().cwd()


try:
    response = requests.get("https://www.automatetheboringstuff.com/files/rj.txt", timeout=5)
    response.raise_for_status()
    print(response.headers["Content-Type"])
    with Path(store_dir / "RomeoAndJuliet.txt").open("wb") as file:
        for chunck in response.iter_content(CHUNK_SIZE):
            file.write(chunck)
except requests.exceptions.HTTPError as e:
    print(f"error: {e}")
except requests.exceptions.ConnectionError:
    print("Couldnt connect to server")


