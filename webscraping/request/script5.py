# demonstrate progress bar creation
from tqdm import tqdm

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

for n in tqdm(range(100000000), colour='green', desc="some message"):
    pass

# 

def count_down(x):
    while True:
        if x < 0:
            break
        yield x
        x -= 1
    
v =count_down(10)

for _ in  tqdm(count_down(10), total=9):
    pass