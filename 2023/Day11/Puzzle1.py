

with open("image.txt") as inFile:
    lines = inFile.readlines()
    lines = list(map(lambda x: [*x.strip()], lines))

    for i, line in enumerate(lines.copy()):
        if line.count("#") == 0:
            lines.insert(i+1, ["."] * 10)
    
    cols = [[row[col] for row in lines] for col in range(len(lines[0]) - 1)]

    extraCols = 0
    for i, col in enumerate(cols):
        if col.count("#") == 0:
            for row in range(len(lines)):
                lines[row].insert(i+1+extraCols, ".")
            extraCols += 1

galaxies = []
for i, line in enumerate(lines):
    print("".join(line))

    if "".join(line).find("#") != -1:
        galaxies.append((i, "".join(line).find("#")))


from itertools import combinations
galaxyPairs = [tuple(sorted(pair)) for pair in combinations(galaxies, 2)]

print(len(galaxyPairs))
for pair in galaxyPairs:
    print(pair)