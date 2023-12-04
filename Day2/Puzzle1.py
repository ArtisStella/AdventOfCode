from utils import *

idSum = 0
maxValues = {"red": 12, "green": 13, "blue": 14}

with open("gameConfig.txt") as inpFile:
    gameInfos = inpFile.readlines()

games = list(map(lambda x: Game(x), gameInfos))

for game in games:
    for colorSet in game.sets:
        for color, value in colorSet.items():
            if maxValues[color] < value:
                break
        else:
            continue
        break
    else:
        idSum += game.gameId

print(idSum)
