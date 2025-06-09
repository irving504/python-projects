# Program Name: Final.py
# My Name: Irving Frausto
# Python 3.12.4
# Date Started - Date Finished : 03/28/2025
# Description:
from random import randint # random list
numList = []
for i in range (10):
    randomNUM = randint(20,30)
    numList.append(randomNUM)
print("Old messy list: ", numList)
for j in range(len(numList)):
    for i in range(len(numList)-1):
                   if numList[i] > numList[i+1]:
                       numList[i], numList[i+1] = numList[i+1], numList[i]
print("Organized list: ",numList)
def num_sum(numList):#define sum first easier
    total = 0
    for i in range(len(numList)):
        total += numList[i]
    return total
outcome_sum = num_sum(numList)
print(f"Sum of numbers in list: {outcome_sum}")
#define avg second harder
def num_avg(numList):
    totalSUM = num_sum(numList)
    avg = totalSUM/len(numList)
    return avg
outcome_avg = num_avg(numList)
print(f"Average of numbers in list: {outcome_avg}")
#find MEDIAN or number in middle
if len(numList) %2 != 0:
    medianIndex = int(len(numList)/2)
    median = numList[medianIndex]
else:
    medianIndex2 = int(len(numList)/2)
    medianIndex1 = medianIndex2 - 1
    median = (numList[medianIndex1]+numList[medianIndex2])/2
print('Median = ', median)
div_by_two = 0 
for num in numList:#prime number & divisible section of notes **slight tweak**
    if num % 2 == 0:
        div_by_two += 1
print(f"Total numbers divisible by 2:{div_by_two}")
'''

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 6/Week 6b/Final.py
Old messy list:  [20, 20, 28, 22, 28, 30, 20, 24, 22, 20]
Organized list:  [20, 20, 20, 20, 22, 22, 24, 28, 28, 30]
Sum of numbers in list: 234
Average of numbers in list: 23.4
Median =  22.0
Total numbers divisible by 2:10

'''
