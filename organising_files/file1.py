from pathlib import Path
from shutil import copy, copytree, move, rmtree
import os
import zipfile

file = Path.cwd() / "file1.txt"

print(file.stat().st_size / 1024**2)

with zipfile.ZipFile(Path.cwd() / "text.zip", "r") as test:
    print(test.getinfo("home/kit/Kitstdios/learning-python/organising_files/file1.txt"))