def count_down(x):
    while True:
        if x < 0:
            break
        yield x
        x -= 1


c = count_down(10)

for i in c:
    print(i)