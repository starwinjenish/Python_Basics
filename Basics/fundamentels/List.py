Computer_Compenent = ['cpu','grapics card','ram','ssd','motherboard','cabinet']
brand = ['amd','nvidia','crusial','samsung','msi','ant-Esport']
data = ['starwin', 21,'male']
food = ['sambar','biriyani','curd rice']

'''
data.append('gamer')
Computer_Compenent += ['powersuply']
Computer_Compenent.extend(['motherboard','cabinet'])
Computer_Compenent.append('moniter')
print(data[-1])
print(data[-3:0])
print(len(data))
print(data)
print(Computer_Compenent)
Computer_Compenent.extend(data)
print(Computer_Compenent)
print('')
data.insert(4,"programer")
print(data)
print('')
data[2:3] = ['student','streamer']
print(data)
num = [1000,876,455667,197645,5263547]
num.reverse()
print(num)
num.sort(reverse=True)
print(num)


nums=[1,2,3,4,5,6,7,8,9,10]
print(sorted(nums,reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
print(mynums)
print('')

mylist = list([1, 'starwin',True])
print(mylist)
'''
#list_Methods
# data.append("india")
# data.insert(1,"jenish")
# data.remove('jenish')

#data.pop() remove last item from list


#print(f"data:{data}".count('21'))
print(f"Computer_Compenent:{Computer_Compenent}")
# print(f"food{food}")

#List_Slicing
# print("first two combonents",Computer_Compenent[0:2])
# print("last two combonents",Computer_Compenent[-2:])

#list iteration
for i in Computer_Compenent:
    print(f"all components:{i}".upper())

#check if
if "amd" in brand:
    print("yes")

