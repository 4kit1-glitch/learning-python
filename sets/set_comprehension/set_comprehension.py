nums = [1, 2, 3, 4, 5, 5, 6, 3, 2, 1, 100]
word = "brontosaurus"

my_set = set() # creates an empty set

print(my_set)
# remove dublicates easily
num_set = {i for i in nums}
letters = {char for char in word}
print(num_set, letters)
#join the letters into a word with no dublicates
new_word = "".join(letters)
print(new_word)