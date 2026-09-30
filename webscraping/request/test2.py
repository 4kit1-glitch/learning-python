x = (x for x in range(10)) # produces a generator obj

# ones the generator is iterated it and discards its content
for i in x:
    print(i)

# this loop doesnt run cause the generator is empty
for i in x:
    print(i)