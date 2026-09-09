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

# matching optional chars

text = "messi scores 2 goalx and mbappe only 1 goalu"

pattern = re.compile(r'\d+\sgoals?')

matches = pattern.findall(text)
print(matches)


# DEMOSTRATING GREEDY AND NON GREEDY ALGORITHMS
text = "HaHaHaHaHaHa"

pattern = re.compile(r'(Ha){2,5}?')
match = pattern.search(text)
print(match)
