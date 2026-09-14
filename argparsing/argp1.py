# arg parsing with sys.argv

import sys

print(sys.argv) # list of passed arguements 

if len(sys.argv) > 1:       # note len will always be >= 1 cause it stores the file path with it
    print(f"number of arguments passed: {len(sys.argv) - 1}")

script_path = sys.argv[0]

print(script_path)

# the problems with this are obvious cause not enough validation
# also a lot of manual work to handle edge cases 

