myList = [70, 64, 43, 27, 41, 45, 21, 86, 50]
upperbound = len(myList)
lowerbound =0
for index in range (lowerbound +1, upperbound):
    key = myList[index]
    place =index-1
    if myList[place] > key:
        while place >= lowerbound and myList[place] >key:
            temp = myList[place+1]
            myList[place+1] =myList[place]
            myList[place] =temp
            place = place-1
        myList[place+1] =key
print(myList)


