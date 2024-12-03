import math
import threading

class GardenSeed:
    def __init__(self, seed_id):
        self.id = seed_id
        self.soil = 0
        self.fertilizer = 0
        self.water = 0
        self.light = 0
        self.temperature = 0
        self.humidity = 0
        self.location = 0

    def __str__(self):
        return f"Seed ID: {self.id}, Soil: {self.soil}, Fertilizer: {self.fertilizer}, Water: {self.water}, Light: {self.light}, Temperature: {self.temperature}, Humidity: {self.humidity}, Location: {self.location}"


seeds = []
fullMap = {"SeedToSoil": [], "SoilToFert": [], "FertToWater": [], "WaterToLight": [], "LightToTemp": [], "TempToHumidity": [], "HumidityToLoc": [] }


with open("garden.txt") as inFile:

    seedRanges = list(map(lambda x : int(x), inFile.readline().split(":")[1].split()))

    inFile.readline()
    lines = inFile.readlines()


lineType = ""
for line in lines:
    if "seed-to-soil" in line:
        lineType = "SeedToSoil"
    elif "soil-to-fertilizer" in line:
        lineType = "SoilToFert"
    elif "fertilizer-to-water" in line:
        lineType = "FertToWater"
    elif "water-to-light" in line:
        lineType = "WaterToLight"
    elif "light-to-temperature" in line:
        lineType = "LightToTemp"
    elif "temperature-to-humidity" in line:
        lineType = "TempToHumidity"
    elif "humidity-to-location" in line:
        lineType = "HumidityToLoc"
    else:
        pairs = line.split()
        if pairs:
            fullMap[lineType].append(list(map(lambda x: int(x), line.split())))


def FindMapping(source, mappingType):
    mappings = fullMap[mappingType]

    for mapping in mappings:
        soilStart, seedStart, mapRange = mapping

        if (seedStart + mapRange >= source) and (seedStart <= source):
            return source - seedStart + soilStart
        
    return source


def ProcessSeedRange(curLowest, index):
    curLowest = math.inf
    
    for mSeed in range(seedRanges[index], seedRanges[index] + seedRanges[index+1]):
        seed = GardenSeed(mSeed)
        seed.soil           = FindMapping(mSeed,            "SeedToSoil")
        seed.fertilizer     = FindMapping(seed.soil,        "SoilToFert")
        seed.water          = FindMapping(seed.fertilizer,  "FertToWater")
        seed.light          = FindMapping(seed.water,       "WaterToLight")
        seed.temperature    = FindMapping(seed.light,       "LightToTemp")
        seed.humidity       = FindMapping(seed.temperature, "TempToHumidity")
        seed.location       = FindMapping(seed.humidity,    "HumidityToLoc")
        
        if seed.location < curLowest:
            curLowest = seed.location

    curLowests[index] = curLowest


threads = []

curLowests = [math.inf] * len(seedRanges)

for i in range(0, len(seedRanges), 2):
    thread = threading.Thread(target=ProcessSeedRange, args=(curLowests, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(curLowests)

