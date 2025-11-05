#user input
# x = input("do you play video games :  ")
# print(x)

#rock paper ceisor game
import sys
import random
from enum import Enum
print("")
class STAR (Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
playerchoice = input ("Enter : \n1 for rock,\n2 for  paper,\n3 for scissor\n\n")
print(playerchoice)
player = int(playerchoice)
computerchoice = random.choice("123")
if player < 1 or player> 3 :
    sys.exit(" hey! kaioombi must enter 1 , 2 or 3")
computer = int(computerchoice)
print("")
print("you chose :" + str(STAR(player)).replace("STAR","") + ":") 
print("python chose :"+str(STAR(computer)).replace("STAR","")  + ":")
if player ==1 and computer ==3:
    print("you win")
elif player == 2 and computer == 1:
    print("you win")
elif player ==3 and computer == 2:
    print("you win")
elif player == computer:
    print("tie game")
else:
    print("python win")

