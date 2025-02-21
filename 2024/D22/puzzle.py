LOOPS = 2000


def getPrice(secret):
    return secret % 10


class SecretNumber:
    MOD_MASK = 0xFFFFFF

    def __init__(self, value) -> None:
        self.value = value
    
    def evolve(self):
        self.value = ((self.value << 6) ^ self.value) & self.MOD_MASK
        self.value = ((self.value >> 5) ^ self.value) & self.MOD_MASK
        self.value = ((self.value << 11) ^ self.value) & self.MOD_MASK

    def getPrice(self):
        return self.value % 10
    
    def __str__(self) -> str:
        return str(self.value)


def findHighestPrices(prices):
    highestPrice = max(prices)
    return highestPrice, prices.index(highestPrice, prices.index(highestPrice)+1)-3


def getChangeSeq(seqStart, prices):
    changes = []
    
    for i in range(seqStart, seqStart + 4):
        changes.append(prices[i] - prices[i-1])

    return tuple(changes)


def getProfit(seq):
    bananasSold = []

    for changeMap in changeMat:
        sold = changeMap.get(seq, 0)
        if sold > 0:
            bananasSold.append(sold)
    
    return sum(bananasSold)


secretMat = []
pricesMat = []
changeMat = []
uniqueChangeSeqs = set()

with open("2024/D22/input.txt") as inFile:
    secretNumbers = [SecretNumber(int(number)) for number in inFile.readlines()]


for i, secret in enumerate(secretNumbers):
    secrets = []
    prices = []
    changeMap = {}

    for _ in range(LOOPS):
        secrets.append(secret.value)
        prices.append(secret.getPrice())
        secret.evolve()

    changes = [0]*4
    for j in range(1, LOOPS):
        changes.pop(0)
        changes.append(prices[j] - prices[j-1])
        
        if j > 3 and tuple(changes) not in changeMap:
            uniqueChangeSeqs.add(tuple(changes))
            changeMap[tuple(changes)] = prices[j]

    secretMat.append(secrets)
    pricesMat.append(prices)
    changeMat.append(changeMap)


highestProfit = 0

for seq in uniqueChangeSeqs:
    profit = getProfit(seq)

    if profit > highestProfit:
        highestProfit = profit

    # print("Seq:", seq, " Current: ", profit, " Highest:", highestProfit)

print("Best Grofit:", highestProfit)
