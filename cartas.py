#IMPORTS
import random

#VARIABLES
GameLoop = True

#THIS FUNCTION PRINTS THE SHUFFLED DECK OF THE PLAYER AND SIMPLY SHUFFLES THE AI'S DECK
def PrintShuffled(x,y):
    Shuffle(x)
    print("Player's Deck: " + str(x))
    Shuffle(y)
    print("")
    
#THIS FUNCTION SHUFFLES THE DECKS
def Shuffle(x):
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

#THIS FUNCTION REPLACES YOUR HAND WITH THE LAST TWO CARDS OF THE DECK
def Discard2(x):
    return x[:-3:-1]

#THIS FUNCTION LETS YOU CHOOSE WHICH CARD TO DISCARD AND THEN REPLACES THAT ONE WITH THE LAST CARD OF THE DECK
def Discard1():
    PlayerChoiceLoop2 = True
    while PlayerChoiceLoop2 == True:
        print("")
        print("Which card do you wish to discard?")
        Card = input("")

        #THIS TRY IS TO COVER THE CASES OF THE Q,J,K,A
        try:
            Card = int(Card)
        except:
            pass
        
        try:
            handPlayer.remove(Card)
            handPlayer.append(DeckPlayer[-1])
            PlayerChoiceLoop2 = False
        except:
            print("This is not a valid option!")
            print("")
    return handPlayer

#THIS FUNCTION SIMPLY LETS YOU PASS AS NO CHANGES NEED TO BE DONE TO EITHER THE DECK OR THE HAND
def Keep():
    pass

#GAME LOOP STARTS HERE
while GameLoop == True:
    #DEFINE THE DECK
    DeckPlayer = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

    #CREATE A SECOND DECK BY COPYING THE VALUES OF THE FIRST ONE
    DeckAI = DeckPlayer.copy()

    #CALL THE FUNCTION TO PRINT THE PLAYER'S SHFULLED DECK.
    PrintShuffled(DeckPlayer, DeckAI)

    #CREATE TWO LISTS WITH THE LAST TWO CARDS OF EACH DECK
    handPlayer, handAI = Fish(DeckPlayer, DeckAI)

    #REMOVE THE DRAWN CARDS FROM THE PLAYER'S DECK
    for i in handPlayer:
        DeckPlayer.remove(i)

    #PRINT THE PLAYER'S AND THE COMPUTER'S CARDS
    print("Player's Cards: " + str(handPlayer))
    print("")

    #INITIALIZE THE PLAYER CHOICE LOOP SO IF THE PLAYER HAS A MISTAKE, HE CAN INTRODUCE THE OPTION AGAIN
    PlayerChoiceLoop = True

    #PRESENT THE CHOICES AND LET THE PLAYER CHOOSE WHICH PLAY HE WANTS
    while PlayerChoiceLoop == True:
        print("1: Discartar Tudo!")
        print("2: Discartar uma das cartas!")
        print("3: Keep your cards!")
        print("Which option do you prefer?")
        PlayerChoice = input("")

        if PlayerChoice == "1":
            handPlayer = Discard2(DeckPlayer)
            PlayerChoiceLoop = False

        elif PlayerChoice == "2":
            Discard1()
            PlayerChoiceLoop = False

        elif PlayerChoice=="3":
            Keep()
            PlayerChoiceLoop = False
        else:
            print("That is not a valid choice. Please try again!")
            print("")
    
    print("")
    print("Now that we're all set, it's time to see who wins!")

    #PRINT BOTH THE PLAYER'S AND THE COMPUTER'S HANDS
    print("")
    print("Your cards are " + str(handPlayer))
    print("The computer's cards are "+ str(handAI))

    #UTILIZING THE COMPARE FUNCTION, COMPARES THE VALUE OF BOTH THE PLAYER AND THE COMPUTER'S HANDS AND PRINTS THE RESULT OF THE GAME
    if Compare(handPlayer,handAI) == -1:
        print("You have lost!")
    elif Compare(handPlayer, handAI) == 1:
        print("You have won!")
    else:
        print("It's a tie!")

    print("")

    #CREATES A NEW LOOP SO THE PLAYER DECIDES IF HE WISHES TO PLAY AGAIN OR NOT
    PlayerChoiceLoop2 = True
    while PlayerChoiceLoop2 == True:
        print("Wanna play again? (Y/N)")
        PlayerChoice2 = input("")

        if PlayerChoice2.lower() == "y":
            PlayerChoiceLoop2 = False
            print("")
            print("")
            print("")
        elif PlayerChoice2.lower() == "n":
            PlayerChoiceLoop2 = False
            GameLoop = False
            print("Have a good one!")
        else:
            print("That's not a valid option!")
            print("")