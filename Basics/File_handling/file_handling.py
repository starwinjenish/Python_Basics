#UseCase of file_handling
# while True:
#       feedback = input("write your feedback: ")
#       with open("user_feedpack.txt","a") as file:
#             file.write(feedback,"\n" )
#             print("thanks for your feedback")


# example of readline()
# with open("user_feedpack.txt",'r') as file:
#     for line in file:
#         print(line)


# with open("user_feedpack.txt","r") as file:
#     while True:
#         lines = file.read()
#         if not lines:
#             break
#         if "starwin" in lines:
#             print("fonud: ",lines.strip())

#using throw away variable (_)
# with open("file.txt") as note:
#     for _ in range(10):
#         print(note.readline().strip())


# #example 1
# with open("input.csv",'r') as ip,  open("output.csv","w") as op:
#     for line in ip:
#         print(line.strip())
#         op.write(line)


# #example 2 
# import csv
# with open('input.csv','r') as file:
#     reader=csv.DictReader(file)
#     for row in reader:
        # print(row["Name"])


#example 3
with open('input.csv','r') as file1:
    read = file1.readlines()
    for line in read[1:]:
        column = line.strip().split(',')
        print(column[3])