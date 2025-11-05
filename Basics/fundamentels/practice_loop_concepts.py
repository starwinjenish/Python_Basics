'''
Write a Python program that loops through a list of numbers and prints:
1.The square of each positive number.
2.The absolute value of each negative number. 
'''
# numbers = [4, -7, 2, -5, 8, -3]
# for i in numbers:
#     if i > 0:
#         print(f"positive square numbers{i**2},") 
#     else:
#         print(f"absolute value number{abs(i)}")

#2.Write a Python program that calculates the sum of all odd numbers and even numbers separately in a given list of integers.
# numbers = [10, 21, 32, 43, 54, 65, 76, 87]
# sum_even = 0
# sum_odd = 0
# for i in numbers:
#     if i % 2 ==0:
#         sum_even += i
#     else:
#         sum_odd += i  
       
# print(f"Sum of even numbers: {sum_even}")
    
# print(f"Sum of odd numbers : {(sum_odd)}")

#Write a Python program that counts how many vowels (a, e, i, o, u) are in a given string.
'''
sentence = "Hello, how are you?"
Num_counts = 0
for i in sentence:
    if i.lower() in "aeiou":
        Num_counts += 1
print(f"Number of vowels:{Num_counts}")


for i in range(0,50):
    if i%2==0:  
       print(i)

#Calculate the sum of all numbers from 1 to n
num = 20
sum1 = 0
for i in range(1,num+1):
    sum1 += i
print("The sum of numbers from 1 to", num, "is:", sum1)

print("/n")
numb = int(input("Enter The Number: "))
total = 0
for i in range (1,numb+1):
    total +=i # increase the value like 1+2+3+$...your input
print("The sum of  number from 1 to",numb,"is",total)
print("\n")

#Print the multiplication table of a number.
user = int(input("enter multipliction Number :"))
num = 0 # dummy 
for i in range(1,11):
    print(f"{i}x{user}={i*user}")


 #Count the number of digits in an integer using a loop. 
number = int(input("Enter a Number: "))
if number == 0:
    count = 1
else:
    count = 0
while number !=0:
    number = number //10
    count +=1
print("Number of digits:", count)
'''
from Functions import table

multiplication = table()
print(multiplication)

    




