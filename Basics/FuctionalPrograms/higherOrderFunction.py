# #Higher order Function (hof) is a function that either
# '''
# 1.Takes another function as an output


# Used to Make code more flexible, reusable, and dynamic

# '''
# #example 1

# def gmail_email(username, domain="gmail.com"):
#     return f"{username}@{domain}"

# def ymail_email(username, domain="ymail.com"):
#     return f"{username}@{domain}"

# def hotmail_email(username,domain="hotmail"):
#     return f"{username}@{domain}"


# def Build_Email(username, email_func):
#     return email_func(username)

# print(Build_Email("starwin",gmail_email))
# print(Build_Email("abisha",ymail_email))

# #example 2

# def divide(factors):
#     def number(D):
#         return divide / number
#     return divide 

# num = 10
# num1 = 5

# print(num)

# # 2.Returns a function as its output

# def email_builder(domain):
#     def Build_email(username):
#         return f'{username}@{domain}'
#     return Build_email

# gmail = email_builder("gmail.com")
# print(type(gmail))
# ymail = email_builder("yamail.com")
# hotmail = email_builder("hotmail.com")

# print(gmail("gowthem"))
# print(ymail("starwin"))

'''
 Topic 1: Functions as Arguments
🔸 Q1. Custom Greet Function
Write a function shout(name) that returns the uppercase of "Hello, <name>!".
Then, write another function process_name(func, name) that calls func(name).

Expected Output:
process_name(shout, "Alice") → "HELLO, ALICE!"

'''

def shout(name):
    return f"HELLO {name}"

def process_name(func,name):
    return func(name)

print(process_name(shout,"ALICE!"))

'''
Q2. Math Operation Selector
Write three functions: add(a, b), subtract(a, b), and multiply(a, b).
Then, write a function calculate(func, a, b) that uses the passed function to compute the result
Expected Output:
calculate(add, 5, 3) → 8  
calculate(subtract, 5, 3) → 2  
calculate(multiply, 5, 3) → 15

'''
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b

def calculate(func,a,b):
    return func(a,b)

print(calculate(add,5,3))
print(calculate(subtract,5,3))
print(calculate(multiply,5,3))
    
    