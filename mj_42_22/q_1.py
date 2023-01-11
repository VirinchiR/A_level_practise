global StackData #integer
global StackPointer
StackData = [0,0,0,0,0,0,0,0,0,0] #integer
StackPointer = 0 

def PrintArray():
    global StackData
    global StackPointer
    print(StackPointer)
    for x in range (0, 10):
        print(StackData[x])

def Push(DataToPush):
    global StackData
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = DataToPush
        StackPointer = StackPointer + 1
        return True

#main
StackPointer = 0
StackData = [0,0,0,0,0,0,0,0,0,0]
for x in range(0, 11):
    TempNumber = int(input("Enter a number"))
    if Push(TempNumber) == True:
        print("Stored")
    else:
        print("Stack full")
PrintArray()