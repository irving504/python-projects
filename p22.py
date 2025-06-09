#Program Name: p22.py
#My Name: Irving Frausto
# Date Started - Date Finished : 03/06/2025
# Description: Dice Game that gives 2 random dice numbers (1 to 6) for you & computer
from random import randint
repeat = 0

while True: #ME
    dice_1 = randint(1,6) 
    dice_2 = randint(1,6) 
    P1 = dice_1 + dice_2
    print("You rolled: ", dice_1, "and", dice_2, "(total = ", P1, ")")
  
    dice_3 = randint(1,6)  
    dice_4 = randint(1,6)
    P2 = dice_3 + dice_4
    print ("Computer rolled: ", dice_3, "and", dice_4, "(total=", P2, ")")
    if P1 < P2:
        print ("You loose! :(" )
    elif P1 > P2:
        print ("You win! :)" )
    else:
        if P1 == P2:
            print("Its a tie!")
            
    repeat = input("Want to keep them? (yes/no): ")
    if repeat == "yes":
        repeat = 0# had to use p19 to refresh my memory :)
'''
= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 3/Week 3a/p22.py
You rolled:  2 and 6 (total =  8 )
Computer rolled:  3 and 6 (total= 9 )
You loose! :(
Want to keep them? (yes/no): yes
You rolled:  3 and 2 (total =  5 )
Computer rolled:  6 and 1 (total= 7 )
You loose! :(
Want to keep them? (yes/no): yes
You rolled:  1 and 3 (total =  4 )
Computer rolled:  2 and 6 (total= 8 )
You loose! :(
Want to keep them? (yes/no): yes
You rolled:  6 and 4 (total =  10 )
Computer rolled:  3 and 5 (total= 8 )
You win! :)
Want to keep them? (yes/no): yes
You rolled:  4 and 3 (total =  7 )
Computer rolled:  5 and 2 (total= 7 )
Its a tie!
Want to keep them? (yes/no): 
'''
