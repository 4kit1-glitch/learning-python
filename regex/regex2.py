import re

text = "hello mr john"
text = "NO way He made other it"
vowel_pattern = re.compile(r'[aeiouAEIOU]')

found_vowels = vowel_pattern.findall(text)

vowel_pattern = re.compile(r'[^aeiou]')

found_vowels = vowel_pattern.findall(text)
