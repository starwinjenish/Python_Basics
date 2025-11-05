'''
Simple Try-Except

python
Copy
Edit
# What happens when a number is divided by zero?
# Add proper exception handling to avoid a crash.
num = 10
denom = 0
result = num / denom
print(result)

'''
#1.
try:
    num = 10
    denom = 0
    result = num / denom
    print(result)
except ZeroDivisionError:
    print("can't divide by zero!")

###############################################################################################################################################
'''
Catching Multiple Exceptions

python
Copy
Edit
# Handle both ValueError and ZeroDivisionError
user_input = input("Enter a number: ")
result = 100 / int(user_input)
print("Result:", result)
'''
#2.
try:
    user_input = input("Enter a number: ")
    result = 100 / int(user_input)
    print("Result:", result)
except ZeroDivisionError:
    print("can't divied by zero")
except ValueError:
    print()