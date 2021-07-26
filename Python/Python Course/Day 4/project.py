# Rock Paper Scissor Game

import random

Scissor = '''
   
   _____ 
 ( (  ) )
  \________,'"""""""""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/

'''
Rock = '''
    _________
---'  _______)
       (_____)
       (_____)
        (____)
---._____(___)
'''
Paper = '''
________________
|               |
|     Paper     |
|               |
|               |
|               |
|               |
|_______________|

'''
game_images = [Rock, Paper, Scissor]

user_choice = int(input(
    "What do you want to choose? Press 0 for Rock, 1 for Paper or 2 For Scissors. "))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer Choose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You pressed the invalid number,You Loose!!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
