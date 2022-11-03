"""     Assignment 1 - Rock Paper Scissor
        Name :: Abhijith Mallya
        USN :: 4SF20CI002
"""
import random
import os
human_choice=0
user_score = computer_score = 0

while(human_choice != 4 ):
    os.system('cls')
    print("HUMAN :: {}\tVS\tCOMPUTER:: {}\n".format(user_score,computer_score))    
    print("1 --> Rock")
    print("2 --> Paper")
    print("3 --> Scissor")
    print("4 --> Exit")

    human_choice = int(input("Enter Choice :: "))
    outcomes = { 1 : "Rock" , 2 : "Paper" , 3 : "Scissor"}
    list_outcomes = list(outcomes.items())
    key , value  = random.choice(list_outcomes)
    print("Computer Choice :: " + value)

    if human_choice == key :
        print("\nTie!")
    elif (human_choice == 1 and key == 3) or (human_choice == 2 and key == 1) or (human_choice == 3 and key == 2):
        user_score = user_score + 1
    else :
        computer_score = computer_score + 1
    input()