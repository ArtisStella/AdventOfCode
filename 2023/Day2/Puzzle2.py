from utils import *
import math

powerSum = 0

with open("gameConfig.txt") as inpFile:
    games = list(map(lambda x: Game(x), inpFile.readlines()))


for game in games:
    minColorValues = {"red": -math.inf, "green": -math.inf, "blue": -math.inf}

    for colorSet in game.sets:
        for color, value in colorSet.items():
            if value > minColorValues[color]:
                minColorValues[color] = value
    
    setPower = minColorValues["red"] * minColorValues["green"] * minColorValues["blue"]
    powerSum += setPower

print(powerSum)
