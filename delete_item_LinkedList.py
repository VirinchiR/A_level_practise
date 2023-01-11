myLinkedList = [1, 2, 3, 4, 5, None, None, None, None, None, None,None]
myLinkedListPointers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1]
startPointer = 4
nullPointer = -1
heapStartPointer = 5
# deleting item in LinkedList

def delete(itemDelete):
    global startPointer, heapStartPointer
    if startPointer == nullPointer:
        print("Linked List is empty")
    else:
        index = startPointer
        while myLinkedList[index] != itemDelete and index != nullPointer:
            oldindex = index
            index = myLinkedListPointers[index]
        if index == nullPointer:
            print("Item", itemDelete, "not found")
        else:
            myLinkedList[index] = None
            tempPointer = myLinkedListPointers[index]
            myLinkedListPointers[index] = heapStartPointer
            heapStartPointer = index
            myLinkedListPointers[oldindex] = tempPointer

delete(5)
print(myLinkedList)