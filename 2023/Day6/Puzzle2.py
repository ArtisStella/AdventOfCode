
raceTime = 0
raceDistance = 0

with open("raceTimes.txt") as inFile:
    raceTimes = inFile.readlines()
        
    raceTime = int("".join(raceTimes[0].split(":")[1].split()))
    raceDistance = int("".join(raceTimes[1].split(":")[1].split()))


print(raceTime, raceDistance)

winSolutions = 0

for heldTime in range(raceTime):

    remainingTime = raceTime - heldTime
    distance = heldTime * remainingTime

    if distance > raceDistance:
        winSolutions += 1

print(winSolutions)
