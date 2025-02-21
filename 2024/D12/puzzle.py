from copy import deepcopy
from itertools import combinations


with open("2024/D12/input.txt") as inFile:
    oFarm = inFile.read()

    plants = list(set(oFarm))
    plants.remove("\n")

    oFarm = [line.strip() for line in oFarm.split("\n")]

    farm = deepcopy(oFarm)
    farmSize = len(oFarm)


directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]


def getRegionStart(plant, visited):
    for i, row in enumerate(farm):
        for j, land in enumerate(row):
            if land != plant:
                continue
            if (i, j) in visited:
                 continue
            return i, j


def getRegions():
    regions = []
    visited = set()
    for plant in plants:
        # print("\nPlant:", plant)

        region = set()

        toVisit = [getRegionStart(plant, visited)]
        while toVisit:
            curLoc = toVisit.pop()
            visited.add(curLoc)
            region.add(curLoc)

            continueRegion = False
            for direction in directions:
                otherPos = (direction[0] + curLoc[0], direction[1] + curLoc[1])

                if not (0 <= otherPos[0] < farmSize and 0 <= otherPos[1] < farmSize):
                    continue

                otherLand = farm[otherPos[0]][otherPos[1]]

                if otherLand == plant:
                    if otherPos not in visited:
                        toVisit.append(otherPos)
                    continueRegion = True
                    if not toVisit:
                        continueRegion = False

            if not continueRegion:
                nextRegion = getRegionStart(plant, visited)
                if nextRegion:
                    toVisit.append(nextRegion)
                regions.append(list(region))
                region = set()

    return regions


def isInBounds(pos):
    return 0 <= pos[0] < farmSize and 0 <= pos[1] < farmSize


corners = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


totalPrice = 0
bulkPrice = 0
regions = getRegions()
for region in regions:
    farm = deepcopy(oFarm)
    plant = farm[region[0][0]][region[0][1]]

    area = len(region)
    perim = 0
    sides = 0

    for spot in region:
        neighbors = []
        for direction in directions:
            dx, dy = (direction[0] + spot[0], direction[1] + spot[1])

            if not isInBounds((dx, dy)) or farm[dx][dy] != plant:
                perim += 1
                continue

            neighbors.append((dx, dy))

        if len(neighbors) == 0:
            sides += 4

        if len(neighbors) == 1:
            sides += 2
        
        neighborPairs = list(combinations(neighbors, 2))
        for n1, n2 in neighborPairs:
            x1, y1 = n1
            x2, y2 = n2

            if x1 == x2 or y1 == y2:
                continue
            
            if len(neighbors) == 2:
                sides += 1
            
            cx, cy = (x2, y1) if (x2, y1) != spot else (x1, y2)

            if farm[cx][cy] != plant:
                sides += 1

    totalPrice += area * perim
    bulkPrice += area * sides

print("Total Price", totalPrice)
print("Total Price", bulkPrice)