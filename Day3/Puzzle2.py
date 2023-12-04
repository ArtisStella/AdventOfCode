
gearRatioSum = 0
numbers = {}

with open("engineSchematic.txt") as inpFile:
    schematic = inpFile.readlines()
    schematic = list(map(lambda x: x.strip(), schematic))

WIDTH = len(schematic[0])
HEIGHT = len(schematic)


def FindAdjacentNumbers(row, col):
    adjacentNumbers = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue

            dRow, dCol = row + i, col + j

            if not (0 <= dRow < HEIGHT and 0 <= dCol < WIDTH):
                continue

            neighbor = schematic[dRow][dCol]
            # print(dRow, dCol, neighbor)
            if neighbor in "0123456789":
                if neighbor == "7":
                    pass
                for key, value in numbers.items():
                    if neighbor in str(key % 1000):
                        if (dRow, dCol) in value and key not in adjacentNumbers:
                            # print("Found digit match", key)
                            adjacentNumbers.append(key)

    return adjacentNumbers


for row in range(HEIGHT):
    curNumber = ""
    numberSpan = []

    for col in range(WIDTH):
        char = schematic[row][col]

        if char in "0123456789":
            curNumber += char
            numberSpan.append((row, col))

        if (char not in "0123456789" or col + 1 == WIDTH) and len(curNumber) > 0:
            numbers[int(str(row) + str(col) + curNumber.zfill(3))] = numberSpan
            curNumber = ""
            numberSpan = []


myParts = []

for row in range(HEIGHT):
    for col in range(WIDTH):
        char = schematic[row][col]

        if char == "*":
            parts = FindAdjacentNumbers(row, col)


            if len(parts) == 2:
                # print(row, col, char, parts[0] % 1000, parts[1] % 1000)
                gearRatioSum += (parts[0] % 1000) * (parts[1] % 1000)

                myParts.append([(parts[0] % 1000), (parts[1] % 1000)])
    
print(gearRatioSum)

# print(myParts)

# print(FindAdjacentNumbers(90, 78))
# print(numbers[91407])
