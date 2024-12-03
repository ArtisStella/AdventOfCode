
deckValue = 0

with open("cards.txt") as inFile:
    cards = inFile.readlines()
    cards = list(map(lambda x: x.strip(), cards))


for card in cards:
    cardValue = 0

    winningNumbers, yourNumbers = card.split(":")[1].split(" | ")
    winningNumbers = winningNumbers.strip().split()
    yourNumbers = yourNumbers.strip().split()

    for number in yourNumbers:
        if number in winningNumbers:
            cardValue = cardValue * 2 if cardValue > 0 else 1

    deckValue += cardValue

print(deckValue)

