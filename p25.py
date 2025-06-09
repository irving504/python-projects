#Program Name: p25.py
#My Name: Irving Frausto
# Date Started - Date Finished : 03/07/2025
# Description: Write a program that ask the user to input a sentence

sentence = input(f"Please enter a sentence: ")
count1 = 0
count2 = 0
letter1 = input(f"Please enter letter 1:")
letter2= input(f"Please enter letter 2:")
for i in range (0, len(sentence), 1):
    if sentence [i] == letter1:
        count1 += 1
    if sentence [i] == letter2:
        count2 += 1
        
print(letter1, "was found", count1, "times")
print(letter2, "was found", count2, "times")

'''

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 3/Week 3a/p25.py
Please enter a sentence: hello world
Please enter letter 1:e
Please enter letter 2:o
e was found 1 times
o was found 2 times

'''
