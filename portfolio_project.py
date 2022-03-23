'''Import random
Prompt user to pick between (Rock, Paper and Scissors)
Assign the list (rock, paper, scissors) to a variable : option
Prompt the user to pick from the option.
Then another variable “chosen” to random.choice(option)
Creating If statements based on :
ROCK smashes scissors
PAPER covers rock
SCISSORS cuts paper
Else …….
Prompt the user to choose if they would like to play again or exit the game.'''


import random
from portfolio_pkg.otheroptions import gender, play_again
# Put in all the functions related to the came inside the function "the_main_game"
def the_main_game():
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"
    options = [rock, paper, scissors]
    #Name of the player
    username = input("Hey! what's your name?")

    # How many tries a player has defore gameover. Would increase by += 1 if the user wins a round 
    tries = 5

    #imported from the otheroptions.py file
    gender(gen)
    print(f"Welcome to the game of Legends {username}")
    
#Looping through all the options and enabling the user to play as long you don't run out of tries
    while True:
        choices = input(f"Choose an option: 1.{rock}, 2.{paper}, 3.{scissors}")
        #The program's choice
        computers_choice = random.choice(options)
        print(f"The progame chose {computers_choice}")
        if tries == 0:
            break
        if choices == "1" or choices == rock.lower():
            if computers_choice == rock:
                print("You have a tie! Try again")
                tries -= 1
                print(f"You have {tries} tries left")
                continue
            if computers_choice == paper:
                print("You lost this round!")
                play_again()
                tries -= 1
                print(f"You have {tries} tries left") 
            else:
                print(f"You won this round! You go {sex}")
                tries += 1
                print(f"You are rewarded with more play time you! You now have {tries} play time!!!")
        
        elif choices == "2" or choices == paper.lower():
            if computers_choice == paper:
                print("You have a tie! Try again")
                tries -= 1
                print(f"You have {tries} tries left")
                continue
            if computers_choice == paper:
                print("You lost this round!")
                play_again()
                tries -= 1 
                print(f"You have {tries} tries left")
            else:
                print(f"You won this round! You go {sex}")
                tries += 1
                print(f"You are rewarded with more play time you! You now have {tries} play time!!!")
        
        
        elif choices == "3" or choices == scissors.lower():
            if computers_choice == scissors:
                print("You have a tie! Try again")
                tries -= 1
                print(f"You have {tries} tries left")
                continue
            if computers_choice == scissors:
                print("You lost this round!")
                play_again()
                tries -= 1 
                print(f"You have {tries} tries left")
            else:
                print(f"You won this round! You go {sex}")
                tries += 1
                print(f"You are rewarded with more play time you! You now have {tries} play time!!!")
        
                
        else:
            print("Wrong option. Choose from the options shown above")
            continue

          


the_main_game()
                
        


