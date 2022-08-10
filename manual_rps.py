from multiprocessing import RLock
import random



def get_user_choice():                                   # user choice method
    user_choice = input("enter user's choice: " )
    return user_choice

def get_computer_choice():   # computer choice method
    Cchoice = ["rock", "scissor", "paper"]
    computer_choice = random.choice(Cchoice)
    print(f" computer choice:  {computer_choice}")
    return computer_choice
 

def get_winner():    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()        # game winner method
    if user_choice == computer_choice:
        print("Both selected same element: Game tie")
    elif user_choice  ==  "rock" and computer_choice  ==  "paper":
        print("paper can cover rock: computer win")
    
    elif user_choice  ==  "scissor" and computer_choice  ==  "rock":
        print("Rock can smashes scissor: computer win")
    
    elif user_choice  ==  "paper" and computer_choice  ==  "scissor":
        print("Scissor can cut paper: computer win")
    else:
        print("paper can cover rock: user win")


#get_winner()

def play():
    user_choice =get_user_choice()
    computer_choice = get_computer_choice()
    runs = 0
    while runs < 3:
       
        get_winner()
        runs +=1
    if computer_choice > user_choice:
        print("computer won")
    else:
        print("user won")
       # runs += 1
    print("game over")


play()




