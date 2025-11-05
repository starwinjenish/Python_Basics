#for loop
name = ['starwin','jenish','red dead','gta 5 ']
for x in name:
    print(x.upper().title())
print("\n")

#while loop
# correct_pin  = '45637'
# entered_pin = ""
# while  entered_pin != correct_pin:
#     entered_pin = input("Enter The correct pass!")
# print("password Granted")
# print("\n")

#break function
name = ["starwin","sankar","jenish","johan"]
for i in name:
    if i == "jenish":
        break
    print(i)
print("\n")

#continue --(skip and continue)
nums = [12,23,-34,67,-90,89]
for s in nums:
    if s < 0:
        continue
    print(s)

# Get positive numbers only
n = [-23-3,-67,98,-45,90]  
positive_numbers = [num for num in nums if num < 0 ] 
print(positive_numbers)  

# pass concept
n = 1243767
for i in n:
    pass
print("\n")

#usecase of loops
#simple Timer

count  = 10
while count >0:
    print(f"coutdown: {count}")
    count -= 1
print("Hello friend")

#add cart 
items = []
while True:
    item =input("Add item(type 'done' to finish):")
    if item.lower() == 'done':
        break
    items.append(item)
print("your add iteam:",items)


    


