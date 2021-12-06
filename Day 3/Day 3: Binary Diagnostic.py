import math

with open("./Data.txt") as file:
    lines = file.readlines()

newList = []
for element in lines:
    newList.append(element.strip())

vertical = len(newList)
firstBinary = ''
otherWay = ''
intArray = []

for hahahha in newList[0]:
    intArray.append(0)

for xd in range(0, len(newList)):
    for tyr in range(0, len(newList[xd])):
        if int(newList[xd][tyr]) == 1:
            intArray[tyr] = intArray[tyr] + 1

for haha in range(0, len(intArray)):
    if intArray[haha] > math.ceil(vertical/2):
        firstBinary += '1'
    else:
        firstBinary += '0'

for skudud in range(0, len(firstBinary)):
    if firstBinary[skudud] == '0':
        otherWay += '1'
    else:
        otherWay += '0'

firstNumber = int(firstBinary, 2)
secondNumber = int(otherWay, 2)
print("multiplied: " + str(firstNumber*secondNumber))
