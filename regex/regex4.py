import re

# matching everything witht the r'.*' except new line chars
# matching new line chars

text1 = "<be a good boy> mom said>"
text2 = "the federals\nthe president\nladys and gentlemen\nwelcome"

pattern = re.compile(r'<.*?>') # introducing the ? next to the * makes it lazy
match = pattern.search(text1)

# without the re.DOTALL constant passed as arg it doent match /n chars
pattern = re.compile(r'.*', re.DOTALL)
match = pattern.search(text2)


