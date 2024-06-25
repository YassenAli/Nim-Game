import random
print("Welcome in Nim Game, This is a game where players take turns taking stones from a pile of stones. The player who takes the last stone loses.")
User = 0
YourTurn = True
choice = 'y'
while choice == 'y':
    player1 = str(input("please enter your player1 name: ")) # Ask player 1 for his name
    Stones = random.randint(20, 30)
    game_setting = str(input("please choose between 1 vs 1 or vs computer: ").lower()) # Ask if he want to play with computer or with friend
    print("The current stone count is:", Stones)
    if game_setting == "1 vs 1" or game_setting == "1 vs1" or game_setting == "1vs 1" or game_setting == "1vs1" or game_setting == "1":
        player2 = str(input("please enter your player2 name: ")) # Ask player 2 for his name
        while True:
            while YourTurn == True and Stones > 0:
                User1 = int(input("player1, How many stones do you want to remove? "))
                if User1 == 1 or User1 == 2 or User1 == 3 and User1 <= Stones:
                    Stones -= User1
                    print(f"{Player1} removed {User1} stone! The current stone count is: ", Stones)
                    YourTurn = False
                elif User1 != 1 or User1 != 2 or User1 != 3:
                    print(f"Hmmm. {Player1} entered an invalid value, {Player1} can only remove from 1 to 3 stones."
                          "please, Try again")
                elif User > Stones:
                    print("There aren't that many stones left!")  # Give user error!
            # Take turns
            while YourTurn == False and Stones > 0:
                User2 = int(input(f"{player2}, How many stones do you want to remove? "))
                if User2 == 1 or User2 == 2 or User2 == 3 and User2 <= Stones:
                    Stones -= User2
                    print(f"{Player2} removed {User1} stone! The current stone count is: ", Stones)
                    YourTurn = True
                elif User2 != 1 or User2 != 2 or User2 != 3:
                    print(f"Hmmm. {Player2} entered an invalid value, {Player2} can only remove from 1 to 3 stones."
                          "please, Try again")
                elif User > Stones:
                    print("There aren't that many stones left!")  # Give user error!
            # Print the winner
            if Stones <= 0:
                if YourTurn == True:
                    print(f"{Player2} took the last stone it lost. {Player1} won the game!")
                    break
                elif YourTurn == False:
                    print(f"{Player1} took the last stone you lost. {Player2} won the game!")
                    break
    else:
        player2 = "computer"
        while True:
                while YourTurn == True and Stones > 0:
                    User = int(input("How many stones do you want to remove? "))
                    if User == 1 or User == 2 or User == 3 and User <= Stones:
                        Stones -= User
                        print(f"{player1} removed {User} stone! The current stone count is: ", Stones)
                        YourTurn = False
                    elif User != 1 or User != 2 or User != 3:
                        print(f"Hmmm. {player1} entered an invalid value, {player1} can only remove from 1 to 3 stones."
                              "please, Try again")
                    elif User > Stones:
                        print("There aren't that many stones left!") #Give user error!
                # Take turns
                while YourTurn == False and Stones > 0:
                    AI = random.randint(1, 3)
                    if AI == 1 or AI == 2 or AI == 3 :
                        Stones -= AI
                        print(f"Computer removed {AI} stone! The current stone count is: ", Stones)
                        YourTurn = True
                # Print the winner
                if Stones <= 0:
                    if YourTurn == True:
                        print(f"The Computer took the last stone it lost. {player1} won the game!")
                        break
                    elif YourTurn == False:
                        print(f"{player1} took the last stone you lost. The Computer won the game!")
                        break
    choice = input("Do you want to play again? (y/n): ") # Ask if he want to play again