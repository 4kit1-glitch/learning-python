import sys
from pathlib import Path
import requests



def save_webcontent(weburl: str, file_path: Path) -> bool:
    # 1. Get the data FIRST
    try:
        response = requests.get(weburl, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Request failed: {err}")
        return False

    # 2. Check the content type safely
    content_type = response.headers.get("content-type", "")
    if "html" not in content_type.lower():
        print(f"Invalid content type: {content_type}")
        return False

    try:
        with file_path.open("w", encoding="utf-8") as f:
            f.write(response.text)
        return True
        
    except OSError as err:
        print(f"Failed to write to {file_path}: {err}")
        return False


if __name__ == "__main__":
    print("Invalid use")
    sys.exit(1)