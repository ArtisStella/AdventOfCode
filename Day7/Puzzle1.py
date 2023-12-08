

hands = []
deckTypeToPower = {"Five of a kind": 6, "Four of a kind": 5, "Full house": 4, "Three of a kind": 3, "Two pair": 2, "One pair": 1, "High card": 0}
cardStrength = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}


class Hand:
    def __init__(self, handStr) -> None:
        self.cards, self.bid = handStr.split()
        self.bid = int(self.bid)
        self.deckType = self._getDeckType()
    
    def _getDeckType(self):
        cardCounts = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for card in set(self.cards):
            cardCounts[self.cards.count(card)] += 1
        
        countCode = "".join(map(lambda x: str(x), cardCounts.values()))

        deckType = ""
        if countCode == "10000":
            deckType = "Five of a kind"
        elif countCode == "01001":
            deckType = "Four of a kind"
        elif countCode == "00110":
            deckType = "Full house"
        elif countCode == "00102":
            deckType = "Three of a kind"
        elif countCode == "00021":
            deckType = "Two pair"
        elif countCode == "00013":
            deckType = "One pair"
        elif countCode == "00005":
            deckType = "High card"

        return deckType

    def __gt__(self, other):
        deckPower = deckTypeToPower[self.deckType]
        otherDeckPower = deckTypeToPower[other.deckType]
        
        if deckPower > otherDeckPower:
           return True
        elif deckPower == otherDeckPower:
            for i in range(len(self.cards)):
                cardStr = cardStrength[self.cards[i]]
                otherStr = cardStrength[other.cards[i]]
                if cardStr > otherStr:
                    return True
                elif cardStr < otherStr:
                    break
    
        return False


with open("deck.txt") as inFile:
    hands = list(map(lambda x: Hand(x), inFile.readlines()))


hands = sorted(hands)
sumBids = 0

for i, hand in enumerate(hands):
    print(i+1, hand.cards, hand.bid, hand.deckType, (i+1)*hand.bid)
    sumBids += (i+1) * hand.bid

print(sumBids)
