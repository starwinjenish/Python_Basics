import random
import sys
print("")
player_choice = int(input("Enter :\n 1.ODD\n 2.EVEN \n \n "))
print("")
player_choice = (int(input("Enter the Number :")))
player = player_choice
computer_choice = random.choice("1,2")
if player < 1 or player > 2:
    print(sys.exit("hey....kaioombi must select 1 or 2"))
computer = int(computer_choice)
if player / 2 == 0:
    print("You win")
        


