# Program Name: p46.py
# My Name: Irving Frausto
# Python 3.12.4
# Date Started - Date Finished : 03/21/2025
# Description: program that takes file & 4 movies from user, writes them to file
# reads and shows them as a list, then write the title in reverse order to a new
# file called "reverseOrder.txt"
aFile = input("Please enter file name: ")#STEP 1 & 2
newFile = open(aFile, 'w')
for i in range (4):
    movie = input("Please enter a movie title: ")
    newFile.write(movie+'\n')
newFile.close()
print("Converting movies into file ","'", aFile,"'")

myFile = open(aFile, 'r')#TURNING INPUTS TO LIST
listofLines = myFile.read().splitlines()
myFile.close()

print("Reading the movie titles from file to a list = ", listofLines)

rFile = open('reverseOrder.txt', 'w') #’w’ or write mode = overrides existing data
for i in range(3, -1, -1): #for variable “x” found in range of (3, -1, -1)
    rFile.write(listofLines[i] +'\n')#the variables “newFile” list(s) + ‘\n’ end the line
rFile.close()#end code
print("Movies have bee written in reverse order to 'reverseOrder.txt'.")
#doesnt show reversed list...brain tired :(
print("Content of" , aFile, ":")
myFile = open(aFile, 'r')
print(myFile.read())
myFile.close()

print("Content of reverseOrder.txt:")
rFile = open('reverseOrder.txt', 'r')
print(rFile.read())
rFile.close()

'''

= RESTART: /Users/saulfrausto/Desktop/De Anza College /Intro to Coding - Python/Week 5/Week 5a/p46.py
Please enter file name: myMovies.txt
Please enter a movie title: s
Please enter a movie title: a
Please enter a movie title: u
Please enter a movie title: l
Converting movies into file  ' myMovies.txt '
Reading the movie titles from file to a list =  ['s', 'a', 'u', 'l']
Movies have bee written in reverse order to 'reverseOrder.txt'.
Content of myMovies.txt :
s
a
u
l

Content of reverseOrder.txt:
l
u
a
s

'''

