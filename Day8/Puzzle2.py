from math import lcm


directions = ""
locations = {}

with open("map.txt") as inFile:
    directions = inFile.readline().strip()
    inFile.readline()
    
    for loc in inFile.readlines():
        locKey, nextNodes = loc.split(" = ")
        locations[locKey] = (nextNodes[1:4], nextNodes[6:9])


def findZ(node):
    stepCount = 0
    current = node
    while current[-1] != "Z":
        direction = directions[stepCount % len(directions)]
        nextNodes = locations[current]
        current = nextNodes[0] if direction == "L" else nextNodes[1]
        stepCount += 1
    return stepCount


curLocs = [node for node in locations.keys() if node[-1] == "A"]

print([findZ(node) for node in curLocs])
