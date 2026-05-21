# -*- coding: utf-8 -*-

nums = [2, 4, 7, 5, 6]


num_set = set(nums)
thisset = {"apple", "banana", "cherry"}

print(thisset)
thisset.remove("apple") # remove raises an error if not found
print(thisset)
thisset.discard("papa") # removes element but doesnt raise an err
print(thisset)

set1 = {1, 2, 3}
set2 = {2, 4, 5}

print(set1, set2)

set3 = set1.union(set2) # returns a new set
print(set1, set2, set3)

print(set1 == set3)

# keep similar only
set4 = set1.intersection(set2)
print(set4)

set3.intersection_update(set2)
print(set3)