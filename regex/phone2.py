import re

# matching regecx has basically 3 steps 
# create the pattern object
# pass pass string to patternobject.search method to called a matched object
# call the matchedobject.group() methon to get the matched string

text = "my number is 677-084-145"

number_pattern_obj= re.compile(r'\d{3}-\d{3}-\d{3}')
matched_obj = number_pattern_obj.search(text)

if matched_obj:
    print(matched_obj.group())
else:
    print("no match")