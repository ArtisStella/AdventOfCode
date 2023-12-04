def ColorSetToMap(colorSet : str):
    colorMap = {}
    colorSet = colorSet.strip().split(", ")

    for color in colorSet:
        colorCount, colorKey = color.split()
        colorMap[colorKey] = int(colorCount)

    return colorMap

class Game:
    def __init__(self, gameStr):
        gameId, colorSets = gameStr.split(":")
        colorSets = colorSets.split(";")

        self.gameId = int(gameId.split()[1])
        self.sets = list(map(lambda colorSet: ColorSetToMap(colorSet), colorSets))
