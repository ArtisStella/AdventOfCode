import heapq

spaceSize = 71

with open("2024/D18/input.txt") as inFile:
    corrupted = [line.strip() for line in inFile.readlines()]

    for i, byte in enumerate(corrupted):
        byte = byte.split(",")
        corrupted[i] = (int(byte[0]), int(byte[1]))


# def print_memory():
#     for line in memorySpace:
#         print(line)


def makeMemorySpace(numBytes):
    corruptedBytes = corrupted[:numBytes]
    space = []
    for i in range(spaceSize):
        row = []
        for j in range(spaceSize):
            if (j, i) in corruptedBytes:
                row.append("#")
            else:
                row.append(".")
        space.append(row)
    return space


start = (0, 0)
end = (spaceSize-1, spaceSize-1)


def heuristic(curPos):
    return abs(curPos[0] - end[0]) + abs(curPos[1] - end[1])


def getToExit(bytesFallen):
    memorySpace = makeMemorySpace(bytesFallen)
    # print_memory()

    cameFrom = {}

    openSet = []
    heapq.heappush(openSet, (0, start))

    gScores = {start: 0}
    fScores = {start: heuristic(start)}

    while openSet:
        _, current = heapq.heappop(openSet)
        # print(current)

        if current == end:
            # print("Ended!")
            path = []
            while current in cameFrom:
                path.append(current)
                current = cameFrom[current]
            path.append(start)
            steps = path[::-1]
            return len(steps) - 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if not (0 <= neighbor[0] < spaceSize and 0 <= neighbor[1] < spaceSize):
                continue

            if memorySpace[neighbor[0]][neighbor[1]] != "#":
                gScoreTemp = gScores[current] + 1

                if neighbor not in gScores or gScoreTemp < gScores[neighbor]:
                    cameFrom[neighbor] = current
                    gScores[neighbor] = gScoreTemp
                    fScores[neighbor] = gScoreTemp + heuristic(neighbor)
                    heapq.heappush(openSet, (fScores[neighbor], neighbor))
                    
    return -1

bytesFallen = 1024
while True:
    noOfSteps = getToExit(bytesFallen)
    print("Solution steps:", noOfSteps, f"{bytesFallen}/{len(corrupted)}")
    if noOfSteps == -1:
        print("No Solution on byte:", corrupted[bytesFallen])
        break
    bytesFallen += 1
    # break
