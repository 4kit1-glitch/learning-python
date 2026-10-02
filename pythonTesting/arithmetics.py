

def add(x, y):
    return x + y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("cant divide by 0")
    return x / y