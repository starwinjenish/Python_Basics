# #Find Item in Array

# arr = [12,23,0,65]
# print(3 in arr)

# #Print all even numbers from array.
# array = [1,2,3,4,5,6,7,8,9]

# for i in array:
#     if i % 2 ==0:
#         print(f'even number {i}')


# #Find the largest number in array.
# int_array = [12,34,67,87,90,43]
# max_arr = array[0]

# for num in int_array:
#     if num > max_arr:
#         max_arr = num
# print(f'The largest number is : {max_arr}')

# #Add all elements (sum of array).

# numb = [12,34,67,87,90,43]

# total= 0

# for i in numb:
#     total += i
# print(total)
        
        
# #Reverse the array.
# array1 = ['starwin','jenish','abisha','allwin']
# array1.reverse()
# print(array1)

# #Question 1: Sum of All Elements
# #Given: [2, 4, 6, 8]

# given = [2, 4, 6, 8]
# total = 0
# for f in given:
#     total += f
# print(total)

#Question 2: Find the Maximum

# List = [14, 3, 25, 7, 19]
# max_num = List[0]

# for i in List:
#     if i > max_num:
#         max_num = i
# print(f'maximum number: {max_num}')



'''
Basic Level

Create a list of 10 numbers and print:

first element

last element

length of the list

Take a list and print all even numbers.

Find the sum and average of all numbers in a list.

Count how many positive and negative numbers are in a list.

Find the maximum and minimum elements without using max() or min().
'''

# arr = [1,2,3,4,5,6,7,8,9,10]
# count = 0
# sum = 0
# print(arr[0])
# print(arr[9])
# print(len(arr))

# even number
'''for i in arr:
    if i % 2 ==0:
        print(f"even number:{i}")'''
'''
#Total sum
for each in arr:
    sum += each
print(sum)

#Average
count1 = len(arr)
average = sum / count1
print(average) # 5.5 '''

# Count how many positive and negative numbers are in a list.  
'''
arr = [-1,3,-6,3,7,-9,45,-46]

pos_num = 0
neg_num = 0

for i in arr:
    if i > 0:
        pos_num += 1
       
    elif i < 0:
        neg_num += 1
        
    else:
        print("0 is not positive and negative")
print(f"Positive numbers:{pos_num}")
print(f"negative numbers:{neg_num}") '''

# Find Maximum and Minimum Element in a List

arr = [1,2,3,4,5,6,7,8,9,10]
# min_value = arr[0]
# max_value = arr[0]

# for i in arr:
#     if i < min_value:
#         min_value = i
#     elif i > max_value:
#         max_value = i

# print(f"max value:{max_value}")
# print(f"Minimum value;{min_value}")

start = 0
end = len(arr)-1

while start < end:
    arr[start],arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)

'''
Q1: Print all elements in a list
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)


👉 What is the time and space complexity?
Time complexity is o(n)

'''


