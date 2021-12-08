import statistics
import math

with open("./Data.txt") as file:
    haha = [int(beep) for beep in file.readline().split(",")]
avg = math.floor(statistics.mean(haha))
totalFuel = 0

for boo in range(2):
    for xd in range(len(haha)):
        totalFuel += (abs(haha[xd]-avg) * (abs(haha[xd]-avg)+1)) / 2
    if boo == 0:
        kek1 = totalFuel
    else:
        kek2 = totalFuel
    avg +=1
    totalFuel = 0

if kek1 > kek2:
    kek3 = kek2
else:
    kek3 = kek1
print(int(kek3))