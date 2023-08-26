print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
tresure_route=(input("you're at a cross road. where do you want to go? 'left' or 'right'\n")).lower()
if tresure_route =='left' :
     print("you cleared the level 1.")
         
     tresure_lake=(input("you come to a lake. there is an island in the middle of the lake. type 'wait' to wait for boat. type 'swim' to swim across.\n")).lower()
     if tresure_lake=='wait':
          
        tresure_island=(input("you arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue.which colour do you choose?\n")).lower()
        if tresure_island=='yellow':
            print("you won the game congratulations")
        else:
            print("Game Over!")
     else:
         print("The shark bites you,Game Over!")
     
else :
    print("you fell in the hole!Game Over")