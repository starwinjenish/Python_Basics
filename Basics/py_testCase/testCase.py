def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cannot divide by zero"
    
print(divide(6,2))