def add(x):
    return x+5

def mul (x):
    return x * 5

def composed(x):
    return mul(add(x))

print(composed(4))