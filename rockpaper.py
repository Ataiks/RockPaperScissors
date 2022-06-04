import random


print("\t\t\tWelcome to Rock Paper Scissors\n")
moves={"R":"Rock", "P":"Paper", "S":"Scissors"}
ms=["R","P","S"]

player=1
comp_move=random.choice(ms)

def usermove():
    choice= input("Make your choice: {} : ".format(ms))
    if choice :
        choice=choice.upper()
        check(comp_move,choice)
    else:
            print("Thanks for NOT playing!")


def check(comp_move,choice):
    if choice in moves.keys():
        print("Player: {}\t : CPU: {}" .format(moves[choice] , moves[comp_move] ))
        if choice == comp_move :
            print("Draw")
            usermove()
        elif choice == "P" and comp_move != "S":
            print("Hurray you Win!")
        elif choice == "S" and comp_move == "P":
            print("You win")
        elif choice == "R" and comp_move == "S":
            print("You win")
        else:
            print("Boohoo you lose")
    else:
        player=input("Invalid choice: Press Enter to Exit")
        if player :
            usermove()

while player:
    usermove()

print("Thanks for Playing!")
