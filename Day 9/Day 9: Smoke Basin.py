result = 0

def checkIfAdjacentIsLarger(arr, _row, _column):
    global result
    print(arr[row][column])
    try:
        if int(arr[row][column-1]) < int(arr[row][column]): #left
            return
    except indexError:
        print('yep')
    try:
        if int(arr[row][column+1]) < int(arr[row][column]): #right
            return
    except indexError:
        print('yep')
    try:
        if int(arr[row-1][column]) < int(arr[row][column]): #up
            return
    except indexError:
        print('yep')
    try:
        if int(arr[row+1][column]) < int(arr[row][column]): #down
            return
    except indexError:
        print('yep')

    result = result + int(arr[row][column])

with open("./smallData.txt") as file:
    haha = [line.strip() for line in file.readlines()]


print(haha)


for row in range(len(haha)):
    for column in range(len(haha[row])):
        checkIfAdjacentIsLarger(haha, row, column)




print("result: " + str(result))