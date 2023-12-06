
times = []
distances = []

with open("raceTimes.txt") as inFile:
    raceTimes = inFile.readlines()

    times = raceTimes[0].split(":")[1].split()
    distances = raceTimes[1].split(":")[1].split()

totalWinningSolutions = 1

for i in range(len(times)):
    winSolutions = 0

    raceTime = int(times[i])
    raceDistance = int(distances[i])

    print("For:", raceTime, raceDistance)

    for heldTime in range(raceTime):

        remainingTime = raceTime - heldTime
        distance = heldTime * remainingTime

        if distance > raceDistance:
            winSolutions += 1
    
    totalWinningSolutions *= winSolutions

print(totalWinningSolutions)
