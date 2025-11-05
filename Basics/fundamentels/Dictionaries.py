#Dictionaries
computer = {"brand":"amd",
            "model":"ryzen",
            "year":2020,
             "Components":["ram","ssd",'motherboard']
            }

studentDetails = {
    
        "std1": {"name1":"starwin jenish","age":"22","identy":"indian"},
        "std2": {"name2":"aran","age":"23","identy":"Vadakan"},
        "std3": {"name3":"abisha","age":"19","identy":"Vadakki"}
    
}

# computer1= dict(brand="intel",model="i9",year=2021)
# print(computer1)
# print(type(computer1))
# print(len(computer1))

# #Accessing Items
# print(computer["brand"])
# print(computer.get("model"))

# #list all keys
# print('')
# print(computer1.keys())

# #list all values
# print(computer.values())
# #list all key/value pair as tuples
# print(computer.items())
# #change values
# computer["model"] = "ryzen 9"
# computer.update({"price":50000})
# print(computer)

#romve items
print(computer["brand"])
print(computer.get("amd"))
print(computer.values())
print(computer.keys())
print("\n")
#iteration
for key,value in computer.items():
    print(key,":",value)
print("\n")
computer.update({"Brand":"Nvidia"})
print(computer)
print('\n')
print(computer["Components"][2]) 
print("\n")
for com in computer["Components"]:
    print(com)
print("\n")
print("student details:",studentDetails["std3"]['age'])
for names,age in studentDetails.items():
    print(names["name1"])
    print(age)