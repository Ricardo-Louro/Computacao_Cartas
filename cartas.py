import random

def Shuffle(x,y):
    random.shuffle(x)
    random.shuffle(y)

def PrintShuffled(x,y):
    print("Player's Deck: " + str(x))
    print("Computer's Deck: " + str(y))
    print("")

def PrintFish(x,y):
    return x[:-3:-1], y[:-3:-1]

def Compare(deck1, deck2):
    sum1 = SumDeck(deck1)
    sum2 = SumDeck(deck2)

    if sum1 > sum2:
        return 1
    elif sum1 < sum2:
        return -1
    else:
        return 0

def SumDeck(deck):
    sumTotal = 0
    for card in deck:
        sumTotal += transformValues(card)
    return sumTotal

def transformValues(card):
    if card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    else:
        return card

DeckPlayer = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
DeckAI = DeckPlayer.copy()

Shuffle(DeckPlayer, DeckAI)
PrintShuffled(DeckPlayer, DeckAI)

handPlayer, handAI = PrintFish(DeckPlayer, DeckAI)

print("Player's Cards: " + str(handPlayer))
print("Computer's Cards: " + str(handAI))
print("")

print("Your result is " + str(Compare(handPlayer, handAI)))