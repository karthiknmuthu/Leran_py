import random

rock = '''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ '''
paper = ''' 
_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|     '''

scissors = '''          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/ '''
game = [rock, paper, scissors]
user_choice = int(
    (input("Enter the option Type 0 for Rock, 1 for Paper, 2 for Scissors\n")))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number , You lose!")
else:
    print(game[user_choice])
computer_choice = random.randint(0, 2)
print("computer choice:")
print(game[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice < computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw")
