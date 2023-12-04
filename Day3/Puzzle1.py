
partSum = 0
partNums = []

with open("engineSchematic.txt") as inpFile:
    schematic = inpFile.readlines()
    schematic = list(map(lambda x: x.strip(), schematic))

WIDTH = len(schematic[0])
HEIGHT = len(schematic)

def AdjacentSymbolFound(row, col):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue

            dRow = row + i
            dCol = col + j

            if not (0 <= dRow < HEIGHT and 0 <= dCol < WIDTH):
                continue

            neighbor = schematic[dRow][dCol]
            
            if neighbor != "."and not neighbor.isalnum():
                return True

    return False


for row in range(HEIGHT):
    curNum = ""
    symbolFound = False

    for col in range(WIDTH):
        char = schematic[row][col]

        if char in "1234567890":
            curNum += char
            
            if AdjacentSymbolFound(row, col) and not symbolFound:
                symbolFound = True

        if (char == "." or not char.isalnum() or col + 1 == WIDTH) and len(curNum) > 0:

            if symbolFound:
                partSum += int(curNum)
                partNums.append(int(curNum))

            curNum = ""
            symbolFound = False


print(partSum)
