import random

DeckPlayer = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
DeckAI = DeckPlayer.copy()

random.shuffle(DeckPlayer)
random.shuffle(DeckAI)

print("Player's Deck: " + str(DeckPlayer))
print("Computer's Deck: " + str(DeckAI))

print("")

print("Player's Cards: " + str(DeckPlayer[-1]) + " and " + str(DeckPlayer[-2]))
print("Computer's Cards: " + str(DeckAI[-1]) + " and " + str(DeckAI[-2]))