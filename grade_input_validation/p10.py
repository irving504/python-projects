# Program Name: p10.py
# My Name: Irving Frausto
# Date Started - Date Completed: 02/22/2025
# Python 3.12.4
# Description: Letter Grades with Input Validation

#NOTE TO SELF: Checks if percent is between 0 and 100;
#               assigns letter grades based on range.


percent = float(input("Please enter your grade percent:"))
if percent < 0 or percent > 100:
   print("invalide percent, must be between 0 to 100")
elif percent >= 90 and percent <= 100:
   print("you have an \"A\" ") # print('you have an "A" ')
elif percent >= 80 and percent <= 90:
   print("you have an \"B\" ") #
elif percent >= 70 and percent <= 80:
   print("you have an \"C\" ")
elif percent >= 60 and percent <= 70:
   print("you have an \"D\" ")
elif percent >= 60:
   print("you have an \"F\" ")
'''

===== RESTART: /Users/saulfrausto/Documents/Intro to Coding - Python/p10.py ====
Please enter your grade percent:80
you have an "B" 

===== RESTART: /Users/saulfrausto/Documents/Intro to Coding - Python/p10.py ====
Please enter your grade percent:-1
invalide percent, must be between 0 to 100

===== RESTART: /Users/saulfrausto/Documents/Intro to Coding - Python/p10.py ====
Please enter your grade percent:75
you have an "C" 

'''
