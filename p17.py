#Program Name: p17.py
#My Name: Irving Frausto
# Date Started: 02/28/2025
# Description: computation of tuition in 10 years...
# ...displays a table of the years and tuition costs.
#IMPORTANT: A loop must be used.
print(" Year:  Tuition Cost: ")
t_cost = 10000
for year in range(1,11): #alternative but doesn't round - print("year =", year, 'expense =', t_cost)
    print(" %2i    $%.2f" %(year, t_cost)) #does round, had to play with previous code
    t_cost += t_cost * 0.05
'''
#alternative

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 2/Week 2B/p17.py
 Year:  Tuition Cost: 
year = 1 expense = 10000
year = 2 expense = 10500.0
year = 3 expense = 11025.0
year = 4 expense = 11576.25
year = 5 expense = 12155.0625
year = 6 expense = 12762.815625
year = 7 expense = 13400.95640625
year = 8 expense = 14071.0042265625
year = 9 expense = 14774.554437890625

**************************************************************

#FIXED

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 2/Week 2B/p17.py
 Year:  Tuition Cost: 
  1    $10000.00
  2    $10500.00
  3    $11025.00
  4    $11576.25
  5    $12155.06
  6    $12762.82
  7    $13400.96
  8    $14071.00
  9    $14774.55
 10    $15513.28

'''
