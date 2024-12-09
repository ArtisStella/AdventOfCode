class MemoryBlock():
    def __init__(self, size, free, data):
        self.size = size
        self.free = free
        self.data = data

class File():
    def __init__(self, fileId, size) -> None:
        self.fileId = fileId
        self.size = size

with open("2024/D9/input.txt") as inFile:
    filesystem = inFile.read().strip()

curId = 0
blocks = list()
memory = []
for i, num in enumerate(filesystem):
    num = int(num)
    if i % 2 == 0:
        if num > 0:
            memory.append(MemoryBlock(num, 0, [File(curId, num)]))
        blocks += [curId] * num
        curId += 1
    else:
        if num > 0:
            memory.append(MemoryBlock(num, num, []))
        blocks += ["."] * num

print("Length", len(memory))
print("Arranging...")

done = False
blockId = len(memory) - 1
while not done:
    movesMade = 0
    block = memory[blockId]

    if block.data:
        for i, leftBlock in enumerate(memory):
            if blockId <= i:
                break

            if leftBlock.free >= block.size:
                leftBlock.data += block.data
                block.data = []
                leftBlock.free -= block.size
                # memory[blockId].data, memory[i].data = memory[i].data, memory[blockId].data
                movesMade += 1
                break
    
    blockId -= 1
    if blockId == 0 and movesMade == 0:
        done = True

compacted = []
compactStr = ""
for block in memory:
    blockStr = []
    
    if block.data:
        for file in block.data:
            compacted +=[file.fileId] * file.size
            blockStr += [str(file.fileId)] * file.size
        
        compacted +=[0] * block.free
        blockStr += ["."] * block.free
    else:
        compacted +=[0] * block.size
        blockStr += ["."] * block.size
    
    compactStr += "".join(blockStr)

# compacted = [block.data for block in memory]
# print(compacted)

print("Calculating Checksum...")
checksum = 0
for i, num in enumerate(compacted):
    num = int(num)
    checksum += num * i

print(checksum)