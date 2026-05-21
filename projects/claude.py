# q1

def is_marked(txt: str) -> bool:
    return txt.startswith("#") or len(txt) == 0

def clean(file_path: str):
    try:
        with open(file_path) as file:
            cleaned_lines = [line for line in file if not is_marked(line.strip())]
        return cleaned_lines
    except FileNotFoundError:
        print("file not found check path")

                
# q2

url = input("Enter the URL: ")

def format_check():
    if url.startswith("http://") or url.startswith("https://") and "@" in  url:
        return True

    