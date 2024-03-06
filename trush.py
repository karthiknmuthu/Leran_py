print('''_                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')
print("Welcome to Tresure Island.")
print("Your mission is to find the treasue.")
choise1 = input(
    "You're at a crossroad, where do you want to go? Type 'left' or 'right'"
).lower()
if choise1 == "left":
    choise2 = input(
        'You\'ve come to a lake.There is an island in the middle of the lake.Type "wait" to wait for a boat.Type "swim" to swim across.'
    ).lower()
    if choise2 == "wait":
        #Gmae will continue
        choise3 = input(
            "You arrvie at the island unharmed.There is a house with 3 doors.One red, one yellow and one blue.Which colour do you choose?"
        ).lower()
        if choise3 == "red":
            print("It's a room full of fire,Gmae Over.")
        elif choise3 == "yelloe":
            print("You found the treasure!You win!")
        elif choise3 == "blue":
            print("You enter a room of beasts.Game Over.")
        else:
            print("You chose a door that does not exist.Game Over.")
    else:
        print("You got attacked by an angry trout.Game Over.")
else:
    print("You felt into a hole. Game Over.")
