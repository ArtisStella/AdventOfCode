# TRIED REWRITING, DONT GOT TIME

class MemoryBlock():
    def __init__(self, size, free, data):
        self.size = size
        self.free = free
        self.data = data
    
    def __str__(self):
        blockStr = []
    
        if self.data:
            blockStr += [str(file) for file in self.data]
            blockStr += ["."] * self.free
        else:
            blockStr += ["."] * self.size
        
        return "".join(blockStr)


class File():
    def __init__(self, fileId, size) -> None:
        self.fileId = fileId
        self.size = size
    
    def __str__(self):
        return "".join([self.fileId] * self.size)


class Memory:
    def __init__(self, blocks=[]):
        self.blocks = blocks
    
    def toList(self):
        outList = []

        for block in self.blocks:
            for file in block.data:
                outList +=  [str(file.fileId)] * file.size
            outList += ["."] * block.free

        return outList


with open("2024/D9/input.txt") as inFile:
    filesystem = inFile.read().strip()

curId = 0
memory = Memory()
for i, num in enumerate(filesystem):
    num = int(num)

    if num < 0:
        continue

    if i % 2 == 0:
        memory.blocks.append(MemoryBlock(num, 0, [File(curId, num)]))
        curId += 1
    else:
        memory.blocks.append(MemoryBlock(num, num, []))


def arrangeMemoryBlocks(blocks, wholeFiles=False):
    arranged = blocks
    done = False
    blockId = len(arranged) - 1
    while not done:
        movesMade = 0
        block = arranged[blockId]

        if block.data:
            for i, leftBlock in enumerate(arranged):
                if blockId <= i:
                    break
                
                if wholeFiles:
                    if leftBlock.free >= block.size:
                        leftBlock.data += block.data
                        block.data = []
                        leftBlock.free -= block.size
                        movesMade += 1
                        break
                else:
                    block.free, leftBlock.free = leftBlock.free, block.free

        blockId -= 1
        if blockId == 0 and movesMade == 0:
            done = True

    return arranged


def calculateChecksum(filesystem):
    checksum = 0

    for i, num in enumerate(filesystem):
        num = int(num)
        checksum += num * i

    return checksum


memory.blocks = arrangeMemoryBlocks(memory.blocks)

blockList = memory.toList()

print("".join(blockList))
pass