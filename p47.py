# Program Name: p47.py
# My Name: Irving Frausto
# Python 3.12.4
# Date Started - Date Finished : 03/22/2025
# Description: generate random numbers, save to file, find median
# (NO built in fuctions like sort or median functions)
'''
NOTES TO SELF:
first step code for random numbers in notes 
second step turn into list **look at p46 for reference**
third step use the 'bubble sort' in notes 
fourth step find median 
'''
#random num
from random import randint
numbers = randint(50,55)
newFile = open('randomNumbers.txt', 'w')
for i in range(numbers):
    newFile.write(str(randint(0,101))+'\n')
newFile.close()
#turn into list
x = []#need empty list
myfile = open('randomNumbers.txt', 'r')
listoflines = myfile.read().splitlines()
myfile.close()

for j in range(0, len(listoflines)-1, 1): 

    for i in range(0, len(listoflines)-1, 1):

        if int(listoflines[i]) > int(listoflines[i+1]): 

            temp = listoflines[i]
            listoflines[i] = listoflines[i+1]
            listoflines[i+1] = temp
if len(listoflines)%2 != 0: # odd number of values in the list
    medianIndex = int ( len(listoflines)/2 ) # 3
    median1 = int(listoflines[medianIndex])
    print ('median1 =', median1 ) # 5
else: 
    medianIndex1 = int ( len(listoflines)/2 ) #3
    medianIndex2 = int ( len(listoflines)/2 ) - 1 #2
    median2 = (int(listoflines[medianIndex1] + listoflines[medianIndex2]))/2 #(2+6)/2=4.0
    print ('median2 =', median2 ) # 4.0
'''

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 5/Week 5a/p47.py
median1 = 45

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 5/Week 5a/p47.py
median1 = 43

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 5/Week 5a/p47.py
median2 = 2525.0

'''
