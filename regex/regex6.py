import re

# case insensitive matching
# this is done with the re.IGNORECASE or re.I arg
pat = re.compile(r'robocop', re.IGNORECASE)
match = pat.search("RoboCop found the missing civilians")

# substituting strings 
# this is done with the sub method
pat = re.compile(r'robocop', re.I)
match = pat.sub("iron man","RoboCop found the missing civilians")


# the back reference used with the sub() to map to groups of patterns
pat = re.compile(r'(Mr|Mrs)\. (\w)\w*')
match = pat.sub(r'\1. \2****',"Mrs. Alice was found at the murder scene of Mr. Derrick")
# you can also use the \g<n> where n i group number

# matching complex regex with verbose mode
# first use r''' ''' to match the long strings
# then pass the re.VERBOSE as second arg to compile it ignores the space chars within patterns
# you can also comment with the verbose mode

pattern = re.compile(r'''
    \+\d{3}|\(\d{3}\) #  area code''', re.VERBOSE)
txt = "he called me with +237 677084145 but his number is +333 659749514"
match = pattern.findall(txt)
print(match)

# you can combine the regex options using the bitwise | or operator
