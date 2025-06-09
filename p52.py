# Program Name: p51.py
# My Name: Irving Frausto
# Python 3.12.4
# Date Started - Date Finished : 03/28/2025
# Description:Basically making a grocery list and summarizing the num & cost
class Item:
    numberItems = 0
    def __init__(self, itemName='apple', itemCost=2.49):
        self.name = itemName
        self.cost = float(itemCost)
        Item.numberItems += 1 #adds to list?
    def showItem(self):#method
        print('item =', self.name, 'cost of item = ', self.cost)
    def setItem(self, itemName, itemCost):
        self.cost = float(itemCost)
        self.name = itemName
    def getitemName(self):
        return self.name
    def getitemCost(self):
        return self.cost
#user input
user_itemName = input("Please name the item you are trying to purchase = ")
user_itemCost = input("Please list the price of said item = ")
user_option = Item()
user_option.setItem(user_itemName, user_itemCost)
user_option.showItem()
#making the cake (objects)
print("The item purchase was: ",user_option.getitemName())
print("Cost of item was: $",user_option.getitemCost())
#make 'new' objects
aItem = Item("egg", 8.50)
aItem.showItem()
print("Added new item to grocery list. Total items", Item.numberItems)
list_1 = Item("orange", 2.00)
list_1.showItem()
print("Added new item to grocery list. Total items", Item.numberItems)
list_2 = Item("pear", 1.50)
list_2.showItem()
print("Added new item to grocery list. Total items", Item.numberItems)

#list
groceryBag = []
groceryBag.append(aItem)
groceryBag.append(list_1)
groceryBag.append(list_2)
print("\nAll items in the grocery bag:")
for i in range(len(groceryBag)):
    groceryBag[i].showItem()
#show the list
totalList = 0
for i in range(len(groceryBag)):
    totalList += groceryBag[i].getitemCost()
    print(f"Total cost of item in the grocery bag:${totalList:.2f}")
    print(f"Total number of item in the grocery list:{Item.numberItems}")
'''

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 6/Week 6a/p52.py
Please name the item you are trying to purchase = apple
Please list the price of said item = 2.49
item = apple cost of item =  2.49
The item purchase was:  apple
Cost of item was: $ 2.49
item = egg cost of item =  8.5
Added new item to grocery list. Total items 2
item = orange cost of item =  2.0
Added new item to grocery list. Total items 3
item = pear cost of item =  1.5
Added new item to grocery list. Total items 4

All items in the grocery bag:
item = egg cost of item =  8.5
item = orange cost of item =  2.0
item = pear cost of item =  1.5
Total cost of item in the grocery bag:$8.50
Total number of item in the grocery list:4
Total cost of item in the grocery bag:$10.50
Total number of item in the grocery list:4
Total cost of item in the grocery bag:$12.00
Total number of item in the grocery list:4


'''
