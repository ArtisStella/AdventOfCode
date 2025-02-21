numpad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

robopad = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}


with open("2024/D21/input.txt") as inFile:
    codes = [code.strip() for code in inFile.readlines()]


def generateMoveMap():
    moveMap = {}
    
    for i in "A0123456789":
        for j in "A0123456789":
            x, y = numpad[i]
            nx, ny = numpad[j]
            offset = (nx - x, ny - y)
            moves = [move for move in offsetToMoves(offset) if not isIllegal(i, False , move)]
            moveMap[i+j] = moves

    for i in "Av<>^":
        for j in "Av<>^":
            x, y = robopad[i]
            nx, ny = robopad[j]
            offset = (nx - x, ny - y)
            moves = [move for move in offsetToMoves(offset) if not isIllegal(i, True , move)]
            moveMap[i+j] = moves

    return moveMap


def isIllegal(curPos, isRobot, move):
    if isRobot:
        if curPos == "A" and move.startswith("<<"):
            return True
        if curPos == "^" and move.startswith("<"):
            return True
        if curPos == "<" and move.startswith("^"):
            return True
    else:
        if curPos == "A" and move.startswith("<<"):
            return True
        if curPos == "0" and move.startswith("<"):
            return True
        if curPos == "1" and move.startswith("v"):
            return True
        if curPos == "4" and move.startswith("vv"):
            return True
        if curPos == "7" and move.startswith("vvv"):
            return True

    return False


def offsetToMoves(offset):
    y, x = offset
    moves = ["", ""]

    if y < 0:
        moves[0] += "^" * abs(y)
    else:
        moves[0] += "v" * abs(y)

    if x < 0:
        moves[0] += "<" * abs(x)
    else:
        moves[0] += ">" * abs(x)
    moves[0] += "A"

    if x < 0:
        moves[1] += "<" * abs(x)
    else:
        moves[1] += ">" * abs(x)
    
    if y < 0:
        moves[1] += "^" * abs(y)
    else:
        moves[1] += "v" * abs(y)
    moves[1] += "A"

    return set(moves)


def getNextSequences(seq, level=1):
    if (seq, level) in cache: return cache[(seq, level)]

    if level == 0:
        nextSeq = len(seq)
    else:
        curBtn = "A"
        nextSeq = 0
        for btn in seq:
            moves = moveMap[curBtn + btn]
            nextSeq += min([getNextSequences(move, level-1) for move in moves])
            curBtn = btn
    
    cache[(seq, level)] = nextSeq
    return nextSeq


moveMap = generateMoveMap()

cache = {}
complexities = []

for code in codes:
    minSeq = getNextSequences(code, 26)
    complexities.append(int(code[:-1]) * minSeq)
    print(code, minSeq, complexities[-1])

print("Total Complexity:", sum(complexities))
