import re

# matching start and end of string uses ^ and $ respectively same with bash
# also has the \b that is a boundary tag

text = "Hello world"
text2 = "World ender"

text3 = "its a bou"

match = re.compile(r'^H.+').search(text)
ends_with_vowel = re.compile(r'.*[aeiou]$').search(text3)

# practicing with the \b 
# it works with word boundaries the \B is for within
# that is match anything that is not a word boundary
# good way for working with inside text matching


text = "the cat found a catapult catalog in the catacombs."

match = re.compile(r'\bf.*d\b').findall(text)
print(match)
