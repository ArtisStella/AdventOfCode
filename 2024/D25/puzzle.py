locks = []
keys = []

with open("2024/D25/input.txt") as inFile:
    inp = inFile.read().split("\n\n")

    for item in inp:
        lines = item.split("\n")
        isKey = len(set(lines[0])) == 1 and lines[0][0] == "#"

        flipped = [list(row) for row in zip(*lines)]
        if isKey:
            counts = [col.count("#") - 1 for col in flipped]
            locks.append(counts)
            print("Lock", counts)
        else:
            counts = [col.count("#") - 1 for col in flipped]
            keys.append(counts)
            print("Key", counts)

print()

fits = 0
for key in keys:
    for lock in locks:
        for i in range(len(key)):
            if key[i] + lock[i] > 5:
                # print(lock, key, i, "overlap")
                break
        else:
            # print(lock, key, "fit")
            fits += 1

print("Total Fits:", fits)
