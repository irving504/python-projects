#Program Name: p13.py
#My Name: Irving Frausto 
#Date Started - Date Completed: 02/27/2025
# Python 3.12.4
# Description: converts cents to quaters, dimes, nickles, & pennies

# user enters this, so change it to input
totalCents = int(input('enter total cents:'))

# use integer division to get a whole number for quarters:
quarters = int(totalCents/25) # int(66/25) is 2

# if there are any quarters...
if quarters > 0: # more than zero quarters
    # show how many quarters they have
    print ('you have', quarters, 'quarters')
    # now subtract the quarters from total cents
    totalCents = totalCents - quarters*25 #totalCents=66-2*25=15
    # ^ new value for the remaining total cents

dimes = int(totalCents/10) # int(15/10) is 1
# if there are any dimes...
if dimes > 0: # more than zero dimes
    # show how many dimes they have
    print ('you have', dimes, 'dimes')
    # now subtract the dimes from total cents
    totalCents = totalCents - dimes*10 # totalCents=15-1*10=5
    # ^ new value for the remaining total cents
nick = int(totalCents/5)
if nick > 0:
    print('you have', nick, 'nickels')
    totalCents = totalCents - nick*5
    
pen = int(totalCents/1)
if pen > 0:
    print('you have', pen, 'pennies')
    totalCents = totalCents - pen*1

# NOTE TO SELF: this code esentially takes left over... 
#...cents and converts it into other units
'''

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 2/Week 2A/p13.py
enter total cents:88
you have 3 quarters
you have 1 dimes
you have 3 pennies

'''
