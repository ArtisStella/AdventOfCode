with open("2024/D11/input.txt") as inFile:
    stones = [int(stone) for stone in inFile.read().strip().split()]

print(stones)

loopCount = 75

def blink(stones, level = 0):
    if level == loopCount:
        return stones

    nextStones = {}

    for stone, count in stones.items():
        numStr = str(stone)
        if stone == 0:
            nextStones[1] = nextStones.get(1, 0) + count
        elif len(numStr) % 2 == 0:
            half = len(numStr) // 2
            leftHalf = int(numStr[:half])
            rightHalf = int(numStr[half:])
            nextStones[leftHalf] = nextStones.get(leftHalf, 0) + count
            nextStones[rightHalf] = nextStones.get(rightHalf, 0) + count 
        else:
            nextStones[stone*2024] = nextStones.get(stone*2024, 0) + count

    return nextStones


stoneMap = {}
for stone in stones:
    if stone in stoneMap:
        stoneMap[stone] += 1
    else:
        stoneMap[stone] = 1

for _ in range(loopCount):
    stoneMap = blink(stoneMap)

print(sum(stoneMap.values()))