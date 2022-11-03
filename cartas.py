#IMPORTS
import random

#THIS FUNCTION PRINTS THE SHUFFLED DECKS
def PrintShuffled(x,y):
    print("Player's Deck: " + str(Shuffle(x)))
    print("Computer's Deck: " + str(Shuffle(y)))
    print("")
    
#THIS FUNCTION SHUFFLES THE DECKS
def Shuffle(x,):
    random.shuffle(x)

#THIS FUNCTION RETURNS TWO LISTS, ONE FOR THE LAST TWO CARDS OF EACH DECK
def Fish(x,y):
    return x[:-3:-1], y[:-3:-1]

#THIS FUNCTIONS COMPARES THE SUM OF THE DECKS AND RETURNS THE FINAL VALUE
def Compare(deck1, deck2):
    sum1 = SumDeck(deck1)
    sum2 = SumDeck(deck2)

    if sum1 > sum2:
        return 1
    elif sum1 < sum2:
        return -1
    else:
        return 0

#THIS FUNCTION SUMS THE VALUE OF THE CARDS IN THE PROVIDED LIST
def SumDeck(deck):
    sumTotal = 0
    for card in deck:
        sumTotal += transformValues(card)
    return sumTotal

#THIS FUNCTIONS TRANSFORMS THE VALUES OF EACH NON-NUMBER CARD INTO A NUMBERED VALUE
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


#MAIN PROGRAM STARTS HERE
#DEFINE THE DECK
DeckPlayer = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

#CREATE A SECOND DECK BY COPYING THE VALUES OF THE FIRST ONE
DeckAI = DeckPlayer.copy()

#CALL THE FUNCTION TO PRINT THE SHUFFLED DECKS.
PrintShuffled(DeckPlayer, DeckAI)

#CREATE TWO LISTS WITH THE LAST TWO CARDS OF EACH DECK
handPlayer, handAI = Fish(DeckPlayer, DeckAI)

#PRINT THE PLAYER'S AND THE COMPUTER'S CARDS
print("Player's Cards: " + str(handPlayer))
print("Computer's Cards: " + str(handAI))
print("")

#PRINT THE FINAL RESULT, CALLING THE FUNCTION TO COMPARE THE VALUE OF THE LAST TWO CARDS OF EACH DECK.
print("Your result is " + str(Compare(handPlayer, handAI)))