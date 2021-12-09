with open("./Data.txt") as file:
    haha = file.readlines()
newList = []
for element in haha:
    newList.append(element.strip())
yeeList = []
for word in newList:
    yeeList.append(word.split(" | "))
amountOf174or8 = 0
for xd in range(1, len(yeeList)):
    words = yeeList[xd][1].split(" ")
    for word in words:
        if len(word) in (2, 3, 4, 7):
            amountOf174or8 += 1

print(amountOf174or8)