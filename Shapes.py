# Program Name: Shapes.py
# My Name: Irving Frausto
# Python 3.12.4
# Date Started - Date Finished : 03/15/2025
# Description: write a program that inputs sides & angels to get rectangel, square, or rhombus, positive num too

while True:#MAKES SURE ITS POSIITVE for sides
    print("====","PLEASE PUT SIDES", "====")
    side_a = int(input("Enter 1 side: "))#SIDE NUM
    while side_a < 0:
        side_a = int(input("Re-enter positive number! "))
    side_b = int(input("Enter 2 side: "))
    while side_b < 0:
        side_b = int(input("Re-enter positive number! "))
    side_c = int(input("Enter 3 side: "))
    while side_c < 0:
        side_c = int(input("Re-enter positive number! ")) 
    side_d = int(input("Enter 4 side: "))
    while side_d < 0:
        side_d = int(input("Re-enter positive number! "))
    print("====","PLEASE PUT ANGELS", "====")
    angel_a = int(input("Enter angel a side: "))#ANGEL NUM
    while angel_a < 0:
        angel_a = int(input("Re-enter positive number! "))

    angel_b = int(input("Enter angel b side: "))
    while angel_b < 0:
        angel_b = int(input("Re-enter positive number! "))

    angel_c = int(input("Enter angel c side: "))
    while angel_c < 0:
        angel_c = int(input("Re-enter positive number! "))
        
    angel_d = int(input("Enter angel d side: "))
    while angel_d < 0:
        angel_d = int(input("Re-enter positive number! "))
        
    if side_a == side_b == side_c == side_d and angel_a == angel_b == angel_c == angel_d:#SQUARE
        print("You got a SQUARE!")
    elif side_a == side_b == side_c == side_d:#RECTANGLE
        if angel_a == angel_c and angel_b == angel_d:
            print("You got a RECTANGLE!")
    elif side_a == side_c and side_b == side_d and angel_a == angel_b == angel_c == angel_d:
                print("You got a Rhombus ;) ")
    repeat = input("would you like to repeat? (yes/no): ").lower() #REPEATER
    if repeat != "yes":
           break
'''
= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 4/Shapes.py
==== PLEASE PUT SIDES ====
Enter 1 side: -10
Re-enter positive number! 10
Enter 2 side: -10
Re-enter positive number! 10
Enter 3 side: 10
Enter 4 side: 10
==== PLEASE PUT ANGELS ====
Enter 1 side: 90
Enter 2 side: 90
Enter 3 side: -90
Re-enter positive number! 90
Enter 4 side: -90
Re-enter positive number! 90
You got a SQUARE!
would you like to repeat? (yes/no): yes
==== PLEASE PUT SIDES ====
Enter 1 side: 10
Enter 2 side: 10
Enter 3 side: 10
Enter 4 side: 10
==== PLEASE PUT ANGELS ====
Enter 1 side: 20
Enter 2 side: 30
Enter 3 side: 20
Enter 4 side: 30
You got a RECTANGLE!
= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 4/Shapes.py
==== PLEASE PUT SIDES ====
Enter 1 side: 1
Enter 2 side: -2
Re-enter positive number! 2
Enter 3 side: -1
Re-enter positive number! 1
Enter 4 side: 2
==== PLEASE PUT ANGELS ====
Enter angel a side: 1
Enter angel b side: 1
Enter angel c side: 1
Enter angel d side: 1
You got a Rhombus ;) 
would you like to repeat? (yes/no): 
'''
