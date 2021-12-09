with open("./smallData.txt") as file:
    haha = file.readlines()
newList = []
for element in haha:
    newList.append(element.strip())

amountOf174or8 = 0

for xd in range(1, len(newList), 2):
    words = newList[xd].split(" ")
    for word in words:
        if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
            amountOf174or8 += 1

print(amountOf174or8)