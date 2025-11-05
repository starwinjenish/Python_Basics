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


with open("user_feedpack.txt","r") as file:
    while True:
        lines = file.read()
        if not lines:
            break
        if "starwin" in lines:
            print("fonud: ",lines.strip())

#using throw away variable (_)


   