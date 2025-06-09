# Program Name: p57.py
# My Name: Irving Frausto
# Python 3.12.4
# Date Started - Date Finished : 03/22/2025
# Description: converting amino acid alphabet to output 
myFile = open('aa.txt','r')
linelist = myFile.read().splitlines()
dictionary = {}
for i in range (0,len(linelist),1):
    eachline = linelist[i].split()
    dictionary[eachline[0]] = eachline[1]
myFile.close()
while True:
    sentence = input('Please enter the letter you would like to weight: ')
    sentence = sentence.upper()
    for i in range(0,len(sentence),1):
        if sentence[i] in ('B','J','O','U', 'X', 'Z'):
            break
    else:
        break
sum = 0
for i in range (0,len(sentence),1):
    sum += float(dictionary[sentence[i]])
print('Total weight: %.3f' %sum)
'''

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 5/Week 5b/p57.py
Please enter the letter you would like to weight: skadyek
Total weight: 821.392

'''
