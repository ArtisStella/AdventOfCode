import heapq
from copy import deepcopy


with open("2024/D16/input.txt") as inFile:
    oMaze = [list(line.strip()) for line in inFile.readlines()]
    
    maze = deepcopy(oMaze)
    mazeSize = len(maze)


for i, row in enumerate(maze):
    for j, col in enumerate(row):
        if col == "S":
            start = (i, j)
        if col == "E":
            end = (i, j)


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right


def neighbors(maze, spot, curDir):
    x, y = spot
    for dx, dy in directions:
        if (-dx, -dy) == curDir:
            continue
        neighbor = (x + dx, y + dy)
        if not (0 <= neighbor[0] < mazeSize and 0 <= neighbor[1] < mazeSize):
            continue
        if maze[neighbor[0]][neighbor[1]] != "#":
            moveDir = (dx, dy)
            turnPenalty = 1000 if moveDir != curDir else 0
            yield neighbor, 1 + turnPenalty, moveDir


def printPath(path):
    print()
    maze = deepcopy(oMaze)
    for spot in path:
        maze[spot[0]][spot[1]] = "O"

    for line in maze:
        print("".join(line))
    print()


def heuristic(curPos):
    return abs(curPos[0] - end[0]) + abs(curPos[1] - end[1])


def getToExit(maze, start, end):
    cameFrom = {}
    openSet = []

    heapq.heappush(openSet, (0, 0, start, (0, 1)))

    steps = []
    gScores = {start: 0}
    fScores = {start: heuristic(start)}

    while openSet:
        _, gScoreCurrent, current, dirCurrent = heapq.heappop(openSet)

        if current == end:
            path = []
            while current in cameFrom:
                path.append(current)
                current = cameFrom[current]
            path.append(start)
            steps = path[::-1]
            # return steps, gScores[end], gScores

        for neighbor, newG, newDir in neighbors(maze, current, dirCurrent):
            gScoreTemp = gScoreCurrent + newG

            if neighbor not in gScores or gScoreTemp < gScores[neighbor]:
                cameFrom[neighbor] = current
                gScores[neighbor] = gScoreTemp
                fScores[neighbor] = gScoreTemp + heuristic(neighbor)
                heapq.heappush(openSet, (fScores[neighbor], gScoreTemp, neighbor, newDir))

    return steps, gScores[end], gScores


def findAllPaths(maze, end, bestCost, scores):
    visited = set()

    openSet = []

    heapq.heappush(openSet, (bestCost, end, (0, -1)))
    heapq.heappush(openSet, (bestCost, end, (1,  0)))

    while openSet:
        curG, current, curDir = heapq.heappop(openSet)
        
        if current == (7, 4):
            pass
        
        for neighbor, cost, newDir in neighbors(maze, current, curDir):
            score = scores[neighbor]
            nCost = curG - cost
            
            if score in (nCost - 1000, nCost):
                visited.add(neighbor)
                heapq.heappush(openSet, (nCost, neighbor, newDir))

    visited.add(end)
    return visited


print(start, end)

bestSpots = 0
bestPath, bestCost, scores = getToExit(maze, start, end)
print("Best Cost:", bestCost)

# printPath(bestPath)

uniqueSpots = findAllPaths(maze, end, bestCost, scores)
print("Total Unique Spots:", len(uniqueSpots))
