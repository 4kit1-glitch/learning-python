import re

text = "message me at +237-677-084-145"
text2 = "my number is (677) 084-145"

text3 = "catch me if you can"

text4 = "my number is 677-084-145 and 672-158-900"

phone_pattern_obj = re.compile(r'(\+\d{3})-(\d{3})-(\d{3}-\d{3})')
matched_obj = phone_pattern_obj.search(text)

# matching using excape characters

pt_obj = re.compile(r'(\(\d{3}\)) (\d{3}-\d{3})')
matched_obj = pt_obj.search(text2)

# matching alternate characters 

pattern_obj = re.compile(r'cat(ch|egory)')
matched_obj = pattern_obj.search(text3)


# returning all matches
# search() returns an object to the first matched
# findall() returns an object to the 

phone_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{3}')
matched_obj = phone_pattern_obj.findall(text4)

print(matched_obj)