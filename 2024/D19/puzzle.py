
with open("2024/D19/input.txt") as inFile:
    towels, designs = inFile.read().split("\n\n")

    towels = towels.strip().split(", ")
    designs = designs.split("\n")

# print(towels, designs)


def canFormString(target, substrings, level=0, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if not target:
        return True, [], 1

    leafNodes = 0
    canForm = False
    subsUsed = []
    for sub in substrings:
        if target.startswith(sub):
            didFinish, subs, leafs = canFormString(target[len(sub):], substrings, level + 1, memo)
            if didFinish:
                subsUsed.append([sub] + subs)
                leafNodes += leafs
                canForm = True

    memo[target] = (canForm, subsUsed, leafNodes)
    return memo[target]



possibleDesigns = 0
noOfWays = 0

for i, design in enumerate(designs):
    print("Design:", i)

    colors = set(list(design))
    maxLength = len(design)

    possibleTowels = []
    for towel in towels:
        if len(towel) > maxLength:
            continue
        for color in set(list(towel)):
            if color not in colors:
                break
        else:
            possibleTowels.append(towel)

    # print(canFormString(design, possibleTowels))

    canForm, _, noOfLeaves = canFormString(design, possibleTowels)
    
    if canForm:
        possibleDesigns += 1
        noOfWays += noOfLeaves

print(f"Possible: {possibleDesigns}; Total Ways: {noOfWays}")