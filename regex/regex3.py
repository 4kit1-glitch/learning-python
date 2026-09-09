import re

text = "he gave me 11 balls and 2 balloons"

pattern = re.compile(r'(\d+)\s(\w+)')
matches = pattern.findall(text)
print(matches)

# matching with the . char

text = "the cat sat on the flat mat"

pattern = re.compile(r'.at')
matches = pattern.findall(text)
print(matches)

# atching