from copy import deepcopy

with open("2024/D15/input.txt") as inFile:
    oWarehoue, moves = inFile.read().split("\n\n")

    oWarehoue = [list(line.strip()) for line in oWarehoue.split("\n")]
    warehouse = deepcopy(oWarehoue)
    warehouseSize = len(warehouse)

    moves = moves.replace("\n", "")


def print_warehouse(warehouse):
    for line in warehouse:
        print("".join(line))
    print()


start = (0, 0)
def setStart(warehouse):
    global start
    for i, row in enumerate(warehouse):
        for j, thing in enumerate(row):
            if thing == "@":
                start = (i, j)


dirs = {
    "^": (-1,  0),
    "v": ( 1,  0),
    ">": ( 0,  1),
    "<": ( 0, -1),
}


def thingAt(pos, warehouse):
    return warehouse[pos[0]][pos[1]]

def in_bounds(warehouse, pos):
    width = len(warehouse[0])
    return 0 <= pos[0] < warehouseSize and 0 <= pos[1] < width


def canPush(direction, curPos, warehouse):
    dx, dy = direction
    x, y = curPos
    toMove = []

    # Count boxes in the direction of movement
    while warehouse[x + dx][y + dy] != ".":
        x += dx
        y += dy
        
        if thingAt((x, y), warehouse) == "#":
            return False, []
        
        toMove.append((x, y))
        
    return len(toMove) > 0, toMove


def moveEach(direction, warehouse):
    global curPos
    dx, dy = direction
    push, toPush = canPush(direction, curPos, warehouse)
    
    if not push:
        return warehouse  # No valid move
    
    # Move robot and boxes
    for x, y in toPush:
        warehouse[x + dx][y + dy] = "O"  # Move each box forward
    
    # Move robot
    warehouse[curPos[0]][curPos[1]] = "."
    curPos = (curPos[0] + dx, curPos[1] + dy)
    warehouse[curPos[0]][curPos[1]] = "@"

    return warehouse


def canPushWide(direction, curPos, warehouse):
    dx, dy = direction
    toMove = []

    checkingSpots = [(curPos[0] + dx, curPos[1] + dy)]
    
    # Count boxes in the direction of movement
    while checkingSpots:
        x, y = checkingSpots.pop(0)
        
        if warehouse[x][y] == "." or (x, y) in toMove:
            continue

        if warehouse[x][y] == "#":
            return False, []
        

        if warehouse[x][y] == "[" and dx != 0:
            toMove.append((x, y + 1))
            checkingSpots.append((x + dx, y + 1))
        if warehouse[x][y] == "]" and dx != 0:
            toMove.append((x, y - 1))
            checkingSpots.append((x + dx, y - 1))

        toMove.append((x, y))
        checkingSpots.append((x + dx, y + dy))
        
    return len(toMove) > 0, toMove


def moveEachWide(direction, warehouse):
    global curPos
    dx, dy = direction
    push, toPush = canPushWide(direction, curPos, warehouse)
    
    if not push:
        return warehouse  # No valid move
    
    doReverse = dx + dy > 0
    toPush = sorted(toPush, key=lambda pos: abs(pos[0] * dx) + abs(pos[1] * dy), reverse=doReverse)
    # Move robot and boxes
    for x, y in toPush:
        char = warehouse[x][y]
        warehouse[x + dx][y + dy] = char
        warehouse[x][y] = "."

    # Move robot
    warehouse[curPos[0]][curPos[1]] = "."
    curPos = (curPos[0] + dx, curPos[1] + dy)
    warehouse[curPos[0]][curPos[1]] = "@"

    return warehouse


def make_move(move, warehouse, wide=False):
    global curPos

    dx, dy = dirs[move]
    nextPos = (curPos[0] + dx, curPos[1] + dy)

    if not in_bounds(warehouse, nextPos):
        return warehouse
    
    item = warehouse[nextPos[0]][nextPos[1]]
    if item == "#":
        return warehouse
    elif item == ".":
        warehouse[nextPos[0]][nextPos[1]], warehouse[curPos[0]][curPos[1]] = "@", "."
        curPos = nextPos
    elif wide:
        warehouse = moveEachWide((dx, dy), warehouse)
    else:
        warehouse = moveEach((dx, dy), warehouse)
    
    return warehouse


def part1():
    global curPos

    warehouse = deepcopy(oWarehoue)
    
    print_warehouse(warehouse)
    print(moves, "\n")

    setStart(warehouse)
    print(start, "\n")

    curPos = start

    for move in moves:
        warehouse = make_move(move, warehouse)
        # print_warehouse(warehouse)

    print_warehouse(warehouse)

    sumCoords = 0
    for i, row in enumerate(warehouse):
        for j, thing in enumerate(row):
            if thing == "O":
                sumCoords += i * 100 + j

    print(sumCoords)


def part2():
    global curPos

    warehouse = deepcopy(oWarehoue)
    warehouse = getWideWarehouse(warehouse)
    setStart(warehouse)
    print(start, "\n")

    curPos = start

    for move in moves:
        warehouse = make_move(move, warehouse, True)
        # print_warehouse(warehouse)

    print_warehouse(warehouse)

    sumCoords = 0
    for i, row in enumerate(warehouse):
        for j, thing in enumerate(row):
            if thing == "[":
                sumCoords += i * 100 + j

    print(sumCoords)


def getWideWarehouse(warehouse):
    newWarehouse = []

    for row in warehouse:
        newRow = []

        for col in row:
            if col == ".":
                newRow.append(".")
                newRow.append(".")
            if col == "#":
                newRow.append("#")
                newRow.append("#")
            if col == "O":
                newRow.append("[")
                newRow.append("]")
            if col == "@":
                newRow.append("@")
                newRow.append(".")

        newWarehouse.append(newRow)
    return newWarehouse


print("\n\nPart 1")
part1()


print("\n\nPart 2")
part2()