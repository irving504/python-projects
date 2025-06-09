#Program Name: p21.py
#My Name: Irving Frausto
# Date Started: 03/01/2025
# Description: Write a program which calculates most $ penny *2 daily for 30 day
                # OR 1 million dollars!
while True:
    option = input("Which option do you think gives you more money? (a/b) ")
   
    if option == 'a':
        savings = 0.01  
#example from notes it used 1 mill i think?
        for days in range(1, 31):  
            print(f'days {days}: savings = ${savings:.2f}')  
            savings *= 2  # Doubles each day
    elif option == 'b':
        checkings = 1000000
        for days in range (1, 31):# MADE MISTAKE put 'checking' instead of 'days'
            print(f'days {days}: checkings = ${checkings:.2f}')
 # no intrest due being in checkings
    else:
        print("INCORRECT INPUT. Please enter given options")
        continue
    
    repeat = input ("would you like to try again? (yes/no): ")
    if repeat != 'yes':
        break
    
'''
= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 2/Week 2B/p21.py
Which option do you think gives you more money? (a/b) a
days 1: savings = $0.01
days 2: savings = $0.02
days 3: savings = $0.04
days 4: savings = $0.08
days 5: savings = $0.16
days 6: savings = $0.32
days 7: savings = $0.64
days 8: savings = $1.28
days 9: savings = $2.56
days 10: savings = $5.12
days 11: savings = $10.24
days 12: savings = $20.48
days 13: savings = $40.96
days 14: savings = $81.92
days 15: savings = $163.84
days 16: savings = $327.68
days 17: savings = $655.36
days 18: savings = $1310.72
days 19: savings = $2621.44
days 20: savings = $5242.88
days 21: savings = $10485.76
days 22: savings = $20971.52
days 23: savings = $41943.04
days 24: savings = $83886.08
days 25: savings = $167772.16
days 26: savings = $335544.32
days 27: savings = $671088.64
days 28: savings = $1342177.28
days 29: savings = $2684354.56
days 30: savings = $5368709.12
would you like to try again? (yes/no): yes
Which option do you think gives you more money? (a/b) b
days 30: checkings = $1.00
days 30: checkings = $2.00
days 30: checkings = $3.00
days 30: checkings = $4.00
days 30: checkings = $5.00
days 30: checkings = $6.00
days 30: checkings = $7.00
days 30: checkings = $8.00
days 30: checkings = $9.00
days 30: checkings = $10.00
days 30: checkings = $11.00
days 30: checkings = $12.00
days 30: checkings = $13.00
days 30: checkings = $14.00
days 30: checkings = $15.00
days 30: checkings = $16.00
days 30: checkings = $17.00
days 30: checkings = $18.00
days 30: checkings = $19.00
days 30: checkings = $20.00
days 30: checkings = $21.00
days 30: checkings = $22.00
days 30: checkings = $23.00
days 30: checkings = $24.00
days 30: checkings = $25.00
days 30: checkings = $26.00
days 30: checkings = $27.00
days 30: checkings = $28.00
days 30: checkings = $29.00
days 30: checkings = $30.00
would you like to try again? (yes/no): 
'''
