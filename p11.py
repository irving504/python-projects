# Program Name: p11.py
# My Name: Irving Frausto
# Date Started - Date Completed: 02/22/2025
# Python 3.12.4
# Description: Rock, Paper, Scissors

from random import randint
randomNum = randint(1,3) # makes a random number b/w 1 - 3

#need variables associated with values between 1 to 3
rock = 1
paper = 2
scissors = 3
# user input makes more sense if you playing with someone, but robot v human beter
p1 = int(input("please enter 1-Rock, 2-Paper, 3-Scissors:"))
p2 = randint(1,3)

# 3 ways for p2 to win
if p1 == rock and p2 == paper:
    print("p2 wins, paper covers rock")
elif p1 == scissors and p2 == rock:
    print("p2 wins, rock breaks scissors")
elif p1 == paper and p2 == scissors:
    print("p2 wins, scissors cuts paper")
# 3 ways for p1 to win
elif p1 == rock and p2 == scissors:
    print("p1 wins, rock breaks scissors")
elif p1 == paper and p2 == rock:
    print("p1 wins, paper covers rock")
elif p1 == scissors and p2 == paper:
    print ("p1 wins, scissors cut paper")
# 3 ways (or one if you can think of it) for TIE
else:
    print("It's a tie")
'''
===== RESTART: /Users/saulfrausto/Documents/Intro to Coding - Python/p11.py ====
please enter 1-Rock, 2-Paper, 3-Scissors:3
It's a tie

===== RESTART: /Users/saulfrausto/Documents/Intro to Coding - Python/p11.py ====
please enter 1-Rock, 2-Paper, 3-Scissors:1
It's a tie

===== RESTART: /Users/saulfrausto/Documents/Intro to Coding - Python/p11.py ====
please enter 1-Rock, 2-Paper, 3-Scissors:2
p1 wins, paper covers rock

===== RESTART: /Users/saulfrausto/Documents/Intro to Coding - Python/p11.py ====
please enter 1-Rock, 2-Paper, 3-Scissors:3
p1 wins, scissors cut paper
'''
