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
path = input('''You are on a crossroad, the right way leads you towards the forest,
and if you follow the right path you will end up on at a big river.
Which way do you want to take? Choose "left" or "right" 
''')
choice_river = ""
choice_door = ""
if path.lower() == 'right':
    print('''You ended up in a dense forest, after a while you realise that everything starts to look the same.
     You panik and try to find the way back but you are already to deap in the forest. You are lost
     ----GAME OVER----
     ''')
    raise SystemExit
else:
    choice_river = input('''You walk all the way to the river. Finally there you find a little house that seams to belong to a fishers man.
    You want to cross over to the other side of the river. Its unclear when the fisher will be back. Do you want to wait
    and ask him to help you get to the other side of the river or do you want to try to swim?
    Type either "wait" or "swim"
    ''')

if choice_river.lower() == "swim":
    print('''
    Slowly you enter the water. Its nice and refreshing. After a long day it feels good to wash the dirt from your skin.
    You reached about the middle of the river. There suddenly you see something moving towards you. At second glance you realise its a alligator that quickly comes closer and closer. 
    You try to swim back, but you dont manage in time...... Swimming might not have been such a good option after all.
    ----GAME OVER----
    ''')
    raise SystemExit
else: choice_door = input('''
You dont have to wait long until the fisher comes back. You walk towards him and ask if he
 could help you to the other side. He seams friendly and after a while he agrees. You two step on the boat and he starts
 heading towards the other side. "Good that you didnt try to swim to the other side...." he said after a while.
 You wont belive how many people tried this. They all seam to forgett that this river is full of crocodiles." 
 You reach the other side after a few minutes. You thank the man for his kindness and you head towards the forest.
 After a while you reach an old ruin covered in all sorts of plants. You enter the ruins and you find three doors
 on the inside. Which door do you want to enter? "left", "right" or "infront" ? 
  ''')

if choice_door.lower() == "left" :
    print('''
    You open the door and enter. It closes right behind you again. In front of you is a hall filled with gold and diamonds! 
    CONGRATULATIONS you found the treasure
    ''')
else: print('''
You open the door and enter. It closes right behind you again. In front of you is a family of cave lions that made itselfe cosy here
    ----GAME OVER----
''')