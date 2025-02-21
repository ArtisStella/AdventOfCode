import heapq
from copy import deepcopy
import time

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


with open("2024/D20/input.txt") as inFile:
    oMaze = [list(line.strip()) for line in inFile.readlines()]
    
    maze = deepcopy(oMaze)
    mazeSize = len(maze)


for i, row in enumerate(maze):
    for j, col in enumerate(row):
        if col == "S":
            start = (i, j)
        if col == "E":
            end = (i, j)


def neighbors(maze, spot):
    x, y = spot
    for dx, dy in directions:
        neighbor = (x + dx, y + dy)
        if not (0 <= neighbor[0] < mazeSize and 0 <= neighbor[1] < mazeSize):
            continue
        if maze[neighbor[0]][neighbor[1]] != "#":
            yield neighbor


def getToExit(maze):
    steps = -1
    openSet = [start]
    closedSet = {start}
    scores = {}

    while openSet:
        current = openSet.pop()
        
        for neighbor in neighbors(maze, current):
            if neighbor not in closedSet:
                openSet.append(neighbor)
                closedSet.add(neighbor)
        
        steps += 1
        scores[current] = steps

    return steps, scores


def scanArea(pos, size):
    x, y = pos
    cheats = {}

    for dx in range(-size, size + 1):
        for dy in range(-size, size + 1):
            if not (abs(dx) + abs(dy) <= size):
                continue
            
            nx, ny = x + dx, y + dy
            if not (0 <= nx < mazeSize and 0 <= ny < mazeSize):
                continue

            spot: str = maze[nx][ny]
            if spot in ".E":
                cheats[(nx, ny)] = track[(nx, ny)]

    return cheats


def runCheats(size=2):
    saved = {}
    for spot, score in track.items():
        jumpSpots = scanArea(spot, size)
        for jPos, cheat in jumpSpots.items():
            dist = abs(jPos[0] - spot[0]) + abs(jPos[1] - spot[1])
            dif = cheat-score-dist
            if dif >= SAVE_THRESH:
                saved[dif] = saved.get(dif, 0) + 1
            
    return saved


SAVE_THRESH = 100

start_time = time.time()
stepScores = {}
print(start, end)
maxSteps, track = getToExit(maze)
print(maxSteps)
print()


cheats = runCheats(20) # remove 20 for part 1

moreThanThresh = 0
for count in cheats.values():
    moreThanThresh += count

print(moreThanThresh)


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
