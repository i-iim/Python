#Start
import random
import math


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices_pc = {"player": player_choice, "computer": computer_choice}
    #dictionary
    return choices_pc
#Funktion

def check_win(player, computer):
    
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "Its a tie"
      
    elif player == "rock" and computer == "paper":
        return "Paper covers rock, you lose!"
    elif player == "paper" and computer == "rock":
        return "Paper covers rock, you win!"
    elif player == "scissors" and computer == "rock":
        return "Rock smashes scissors, you lose!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors, you win!"
    elif player == "paper" and computer == "scissors":
        return "Scissors cut paper, you lose!"
    elif player == "scissors" and computer == "paper":
        return "Scissors cut paper, you win!"

    """"   
    if player = "scissors":
        if computer = "rock":
            return "Rock smashes scissors, you lose!"
        else:
            return "Scissors cut paper, you win!"
    if player = "rock":
        #...
        return "empty"
    else:
        return "failed"
    """        
    #comment block  
    

choices = get_choices()
#print(choices)
result = check_win(choices["player"], choices["computer"])
print(result)
#ausgabe und aufrufen von Funktionen
