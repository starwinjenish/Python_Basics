#Exception handling
#what is exception?
'''
try:
    while True:
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter the second number: "))
        c = num1/num2
        print("result: ",c)
except ZeroDivisionError:
    if num2 == 0:
        print("Division by zero is not allowed.")

'''



#usecase
try:
    print("Welcome to stario-shop ")
    item = int(input("how many item?\n "))
    total_price = 200 * item
    avg_price = total_price / item
    print("average price of per item", avg_price)

# except ZeroDivisionError:
#     print("you can't order 0 item")
except FileNotFoundError:
    print("file not found")
finally:
    print("logout")

print("next code block")
