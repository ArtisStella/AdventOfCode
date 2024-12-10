with open("2024/D10/input.txt") as inFile:
    heightMap = [list(line.strip()) for line in inFile.readlines()]
    matrixSize = len(heightMap)

# print(heightMap)

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

def calculateCharacteristics(heightMap):
    totalScore = 0
    totalRating = 0
    trailHeads = []

    for i, row in enumerate(heightMap):
        for j, col in enumerate(row):
            if col == "0":
                trailHeads.append((i, j))
    
    # print(trailHeads)

    for trail in trailHeads:
        trailEnds = []
        steps = [trail]
        previous = None
        while steps:
            curPos = steps.pop()
            current = heightMap[curPos[0]][curPos[1]]

            if previous == "8" and current == "9":
                trailEnds.append(curPos)
                continue

            for direcition in directions:
                pos = (curPos[0] + direcition[0], curPos[1] + direcition[1])

                if not (0 <= pos[0] < matrixSize and 0 <= pos[1] < matrixSize):
                    continue
                
                nextNum = heightMap[pos[0]][pos[1]]
                if nextNum != "." and int(nextNum) - int(current) == 1:
                    steps.append(pos)

            previous = current

        totalScore += len(set(trailEnds))
        totalRating += len(trailEnds)

    return totalScore, totalRating


trailScore, trailRating = calculateCharacteristics(heightMap)
print(trailScore, trailRating)