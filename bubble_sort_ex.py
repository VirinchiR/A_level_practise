myList = [70, 64, 43, 27, 41, 45, 21,1,2,3,4,6,67,9,5,86, 50]
top = len(myList)
swap = True
while(swap) or (top > 0):
    swap = False
    for index in range(top - 1):
        if myList[index] > myList[index + 1]:
            temp = myList[index]
            myList[index] = myList[index + 1]
            myList[index + 1] = temp
            swap = True
    top = top - 1
print(myList)