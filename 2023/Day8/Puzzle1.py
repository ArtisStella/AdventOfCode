import re

directions = ""
locations = {}

with open("map.txt") as inFile:
    directions = inFile.readline().strip()
    inFile.readline()
    
    for loc in inFile.readlines():
        locKey, nextNodes = loc.split(" = ")
        locations[locKey] = (nextNodes[1:4], nextNodes[6:9])


curLoc = "AAA"

def findZ(node):
    stepCount = 0
    current = node
    while current != "ZZZ":
        direction = directions[stepCount % len(directions)]
        nextNodes = locations[current]
        current = nextNodes[0] if direction == "L" else nextNodes[1]
        stepCount += 1
    return stepCount


print(findZ(curLoc))

