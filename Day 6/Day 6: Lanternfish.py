lines = ''
with open("./Data.txt") as file:
    lines = ''
    lines = file.readlines()
kek = []
arr = lines[0].split(",")
for eh in arr:
    kek.append(int(eh))

for lmao in range(0,80):
    for tyr in range(0, len(kek)):
        if kek[tyr] > 0:
            kek[tyr] -= 1
        else:
            kek.append(8)
            kek[tyr] = 6

print(len(kek))
