
class Card:
    def __init__(self, cardText):
        self.id = cardText.split(":")[0].split()[1]
        winningNumbers, yourNumbers = cardText.split(":")[1].split(" | ")
        self.winningNumbers = winningNumbers.strip().split()
        self.yourNumbers = yourNumbers.strip().split()
        self.winCount = 0
        self.value = 0
        self.copies = 1
        self.calculateValue()

    def calculateValue(self):
        for number in self.yourNumbers:
            if number in self.winningNumbers:
                self.value = self.value * 2 if self.value > 0 else 1
                self.winCount += 1
    
    def __str__(self):
        return f"Card {self.id} | Value: {self.value} | Copies: {self.copies}"


deckValue = 0


with open("cards.txt") as inFile:
    cards = inFile.readlines()
    cards = list(map(lambda x: Card(x.strip()), cards))
    

for i, card in enumerate(cards):
    print(card, "| Wins:", card.winCount)

    for j in range(card.winCount):
        subCard = cards[j+i+1]
        subCard.copies += 1 * card.copies
        print("\t" + str(subCard))


print("\nAfter processing")
totalCards = 0
for card in cards:
    print(card)
    totalCards += card.copies

print(totalCards)
