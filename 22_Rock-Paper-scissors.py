#Rock paper scissors.
# Build a rock-paper-scissors game logic using if-else.
import random
print("1 for Rock")
print("2 for Paper")
print("3 for scissors")
robo=random.randint(1,3)
choice=int(input("->> "))
if choice==1 and robo==2:
    print("You lose!")
    print("Robo choice: ",robo)
elif choice==2 and robo==3:
    print("You Lose!")
    print("Robo choice: ",robo)
elif choice==3 and robo==1:
    print("you lose!")
    print("Robo choice: ",robo)
elif robo==1 and choice==2:
    print("You win")
    print("Robo choice: ",robo)
elif robo==2 and choice==3:
    print("You win")
    print("Robo choice: ",robo)
elif robo==3 and choice==1:
    print("You win")
    print("Robo choice: ",robo)
else:
    print("please eneter 1 to 3!!")