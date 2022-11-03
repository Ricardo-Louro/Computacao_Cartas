import random

def Shuffle(x,y):
    random.shuffle(x)
    random.shuffle(y)

def PrintShuffled(x,y):
    print("Player's Deck: " + str(x))
    print("Computer's Deck: " + str(y))

def PrintFish(x,y):
    print("Player's Cards: " + str(x[-1]) + " and " + str(y[-2]))
    print("Computer's Cards: " + str(x[-1]) + " and " + str(y[-2]))

DeckPlayer = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
DeckAI = DeckPlayer.copy()

Shuffle(DeckPlayer, DeckAI)
PrintShuffled(DeckPlayer, DeckAI)
PrintFish(DeckPlayer, DeckAI)