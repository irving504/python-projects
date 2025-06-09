#Program Name: p23.py
#My Name: Irving Frausto
# Date Started - Date Finished : 03/06/2025
# Description: math program that lets student pratice basic math :0

from random import randint

while True:
    num1 = randint(0,10)
    num2= randint(0,10)
    op = int(input("Want to add (1), sub (2), mul (3)?: "))

    if op == 1:
        answer_1 = int(input(f"What is {num1} + {num2} = "))
        while answer_1 != num1 + num2:
            answer = int(input(f"Incorrect. Try again: {num1} + {num2} = "))
    elif op == 2:
        answer_2 = int(input(f"What is is {num1} - {num2} = "))
        while answer_2 != num1 - num2:
            answer = int(input(f"Incorrect. Try again: {num1} - {num2} = "))
    if op == 3:
        answer_3 = int(input(f"What is is {num1} * {num2} = "))
        while answer_3 != num1 * num2:
            answer = int(input(f"Incorrect. Try again: {num1} * {num2} = "))
    repeat = input("You got it! Do you want to play again? (y/n): ")
    if repeat == 'n':
        break 
'''
= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 3/Week 3a/p23.py
Want to add (1), sub (2), mul (3)?: 3
What is is 10 * 10 = 100
You got it! Do you want to play again? (y/n): y
Want to add (1), sub (2), mul (3)?: 1
What is 8 + 4 = 12
You got it! Do you want to play again? (y/n): y
Want to add (1), sub (2), mul (3)?: 2
What is is 1 - 5 = -4
You got it! Do you want to play again? (y/n): 
'''
        
