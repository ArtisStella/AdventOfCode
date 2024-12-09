import re

with open("2024/D9input.txt") as inFile:
    filesystem = inFile.read().strip()

curId = 0
blocks = list()
for i, num in enumerate(filesystem):
    num = int(num)
    if i % 2 == 0:
        blocks += [curId] * num
        curId += 1
    else:
        blocks += ["."] * num


print("Length", len(blocks))
print("Arranging...")

lastReplace = 0
result = blocks
left, right = 0, len(result) - 1

while left < right:
    if result[left] == ".":
        while left < right and result[right] == ".":
            right -= 1
        
        if left < right:
            result[left], result[right] = result[right], result[left]
            # print("".join(result))
            right -= 1
    left += 1


# with open('outputHtml.txt', 'w') as outfile:
#     outfile.write(str(blocks))
#     outfile.write("\n\n")
#     outfile.write(str(result))

compacted = [num for num in result if num != "."]
# print(compacted)

print("Calculating Checksum...")
checksum = 0
for i, num in enumerate(compacted):
    num = int(num)
    checksum += num * i

print(checksum)
