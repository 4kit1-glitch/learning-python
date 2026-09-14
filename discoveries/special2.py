import sys
import subprocess
import os

print(sys.argv) # stores the parameters passed to the python run name

def clear():
    subprocess.call('cls' if os.name == "nt" else 'clear')

clear()

print(sys.argv)