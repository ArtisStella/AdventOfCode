
UP, LEFT, RIGHT, DOWN = [(-1, 0), (0, -1), (0, 1), (1, 0)]

loopPipes = []
pipeToDirection = {
    "-": {RIGHT: RIGHT, LEFT: LEFT},
    "|": {DOWN: DOWN, UP: UP},
    "7": {RIGHT: DOWN, UP: LEFT},
    "J": {RIGHT: UP, DOWN: LEFT},
    "F": {LEFT: DOWN, UP: RIGHT},
    "L": {LEFT: UP, DOWN: RIGHT}
}


with open("pipes.txt") as inFile:
    pipelines = inFile.readlines()
    start = [(i, line.find("S")) for i, line in enumerate(pipelines) if line.find("S") != -1][0]


def FindPieceFromStart(row, col):
    for dx,dy in [UP, LEFT, RIGHT, DOWN]:
        if (row + dx < 0) or (col + dy) < 0:
            continue

        if pipelines[row + dx][col + dy] != ".":
            tile = pipelines[row + dx][col + dy]
            break
    
    # loopPipes.append((row + dx, col + dy))
    return (row + dx, col + dy, tile, (dx, dy))


loopDone = False
row, col = start
tile = pipelines[row][col]
dirVector = (0, 0)
noOfSteps = []
steps = 0

while not loopDone:

    if tile == "S":
        row, col, tile, dirVector = FindPieceFromStart(row, col)
        steps += 1
    else:
        loopPipes.append((row, col))
        noOfSteps.append(steps)
        nextDirection = pipeToDirection[tile][dirVector]
        row, col, dirVector = row + nextDirection[0], col + nextDirection[1], nextDirection
        tile = pipelines[row][col]
        steps += 1
    
    # print(row, col, tile, dirVector)
    if tile == "S":
        loopDone = True


print(start, loopPipes)
print(0, noOfSteps)
# loopPipes.append(start)


# for i, row in enumerate(pipelines):
#     for j, col in enumerate(row):
        
#         if (i, j) in loopPipes:
#             distanceToStart = abs(start[0] - i) + abs(start[1] - j)
#             print(distanceToStart, end="")
#         else:
#             print(".", end="")
    
#     print("\n")



for pipe in loopPipes:
    print(pipelines[pipe[0]][pipe[1]])
