
with open("./Data.txt") as file:
    arr = file.readline().split(",")

haha = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for xd in arr:
    haha[int(xd)] += 1

for xd in range(256):
    bla = haha[0]
    haha[0] = haha[1]
    haha[1] = haha[2]
    haha[2] = haha[3]
    haha[3] = haha[4]
    haha[4] = haha[5]
    haha[5] = haha[6]
    haha[6] = bla + haha[7]
    haha[7] = haha[8]
    haha[8] = bla

print(sum(haha))