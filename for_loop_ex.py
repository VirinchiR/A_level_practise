myList = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = int(input("Please enter item to be found"))
found = False
for index in range (len(myList)):
    if (myList[index] == item):
        found = True
if(found):
    print("item found")
else:
    print("item not found")


