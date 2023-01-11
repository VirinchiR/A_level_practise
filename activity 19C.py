my_list = [16, 19, 21, 27, 36, 42, 55, 67, 76, 89]
item= int(input("please enter the item to be found"))
found = False
lowerBound = 0
upperBound = len(my_list) - 1
while (not found) and (lowerBound <= upperBound):
    index = int((upperBound + lowerBound )/2)
    if (my_list[index] == item):
       found = True
    if item > my_list[index]:
        lowerBound = index+1
    if item < my_list[index]:
        upperBound = index-1
if (found):
    print("item found!")
else:
    print("item not found")
