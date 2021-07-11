import random
game=1

list=["snake","gun","water"]
computer_points=0
player_points=0

while(game<=10 and computer_points<=10 and player_points<=10):
    player = input("whats your choice? s=snake,w=water,g=gun\n")

    computer = random.choice(list)
    if player=="s":
        print("player is","snake")
        print("computer is",computer)
        if computer=="snake":
            print("match is draw")

        elif computer == "gun":
            print("you are lose")
            computer_points += 1
            print("computer points",computer_points,"player points",player_points)
        elif computer=="water":
            print("you are won")
            player_points+=1
            print("player points", player_points,"computer points", computer_points)

    if player == "g":
        print("player is", "gun")
        print("computer is", computer)
        if computer == "snake":
            print("you are won")
            player_points += 1
            print("computer points", computer_points, "player points", player_points)

        elif computer == "gun":
            print("match is draw")

        elif computer == "water":
            print("you are lose")
            computer_points += 1
            print("player points", player_points, "computer points", computer_points)

    if player == "w":
        print("player is", "water")
        print("computer is", computer)
        if computer == "snake":
            print("you are lose")
            computer_points += 1
            print("computer points", computer_points, "player points", player_points)

        elif computer == "water":
            print("match is draw")

        elif computer == "gun":
            print("you are won")
            player_points += 1
            print("player points", player_points, "computer points", computer_points)

    print(game, "chance")
    game += 1



if (game >= 10):
   print("game is up")
if(player_points>computer_points):
 print("you are won","your points",player_points)

if (computer_points > player_points):
 print("you are lose", "computer points", computer_points)







































