import statistics

with open("./Data.txt") as file:
    haha = [int(beep) for beep in file.readline().split(",")]
median = statistics.median(haha)
totalFuel = 0

for xd in range(len(haha)):
    totalFuel += abs(haha[xd]-median)

print(int(totalFuel))
