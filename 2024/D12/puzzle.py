from copy import deepcopy


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

print(plants)
for line in farm:
    print(line)


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


print("\n")
totalPrice = 0
numSides = 0
regions = getRegions()
for region in regions:
    farm = deepcopy(oFarm)
    plant = farm[region[0][0]][region[0][1]]
    print("Plant:", plant)

    area = len(region)
    perim = 0

    edges = {}
    for spot in region:
        edges[spot] = []

        for direction in directions:
            otherSpot = (direction[0] + spot[0], direction[1] + spot[1])

            if 0 <= otherSpot[0] < farmSize and 0 <= otherSpot[1] < farmSize:
                otherLand = farm[otherSpot[0]][otherSpot[1]]
                if otherLand != plant:
                    perim += 1
                    if direction == (-1, 0):
                        edges[spot].append("TOP")
                    if direction == (1, 0):
                        edges[spot].append("BOTTOM")
                    if direction == (0, -1):
                        edges[spot].append("LEFT")
                    if direction == (0, 1):
                        edges[spot].append("RIGHT")
            else:
                if 0 > otherSpot[0]:
                    edges[spot].append("TOP")
                if otherSpot[0] >= farmSize:
                    edges[spot].append("BOTTOM")
                if 0 > otherSpot[1]:
                    edges[spot].append("LEFT")
                if otherSpot[1] >= farmSize:
                    edges[spot].append("RIGHT")
                perim += 1
    
    print(edges)
                
    noOfEdges = 0
    counted = set()
    for spot, curEdges in edges.items():
        if noOfEdges == 0:
            for e in curEdges:
                if e == "LEFT":
                    counted.add(str(spot[1]) + e)
                if e == "RIGHT":
                    counted.add(str(spot[1]) + e)
                if e == "TOP":
                    counted.add(str(spot[0]) + e)
                if e == "BOTTOM":
                    counted.add(str(spot[0]) + e)

            noOfEdges = len(curEdges)
        
        for direction in directions:
            otherSpot = (direction[0] + spot[0], direction[1] + spot[1])
            if otherSpot not in edges:
                continue
            
            for e in edges[otherSpot]:
                if str(otherSpot[0]) + e in counted or str(otherSpot[1]) + e in counted:
                    continue
                
                if e == "LEFT":
                    counted.add(str(otherSpot[1]) + e)
                if e == "RIGHT":
                    counted.add(str(otherSpot[1]) + e)
                if e == "TOP":
                    counted.add(str(otherSpot[0]) + e)
                if e == "BOTTOM":
                    counted.add(str(otherSpot[0]) + e)

                if e not in curEdges:    
                    noOfEdges += 1
                    # edges[spot].remove(e)

    print("No of Edges:", noOfEdges)
    print()

    # print("Area:", area, " Perimiter:", perim)
    totalPrice += area * perim

print("Total Price", totalPrice)
