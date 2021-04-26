import random

# import data from .txt file read first line only print in sorted order highest to lowest

score = 0

file=open(highscores.txt, "r",)
for i in range(0, 2):
    name = file.readlines(int+str)
    file.read(str(score)+name+"\n")
    file.close()

file = open("highscores.txt","r")
readthefile = file.readlines()
sortedData = sorted(readthefile,reverse= True)

print("top 3 scores!")
print("pos\tpoints, Name")