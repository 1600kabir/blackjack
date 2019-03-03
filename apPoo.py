from random import randint

cards = {1: "Ace", 11: "Ace", 10: "King", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11]

userTotal = 0
cardlist = []
card1 = randint(1, 11)
card2 = randint(1, 11)
userTotal = card1 + card2
cardlist = [cards[card1], cards[card2]]

cpuTotal = 0
cpuCardlist = []
cpuCard1 = randint(1, 11)
cpuCard2 = randint(1, 11)
cpuTotal = card1 + card2
cpuCardlist = [cards[card1], cards[card2]]

def check_card(n):
    if n in deck:
        deck.remove(n)
        return True
    else:
        return False

def get_card():
    g = False
    n = randint(1, 11)
    while not g:
        check = check_card(n)
        if check:
            break
    return n

def get_card_dealer():
    p = False
    n = randint(1,11)
    while not p:
        check = check_card(n)
        if check:
            return n

def check(userTotal):
    if int(userTotal) > 21:
        return True
    else:
        return False


def user(userTotal, cardlist):

    print ("Your total is ",userTotal, "You have", cardlist)
    if check(userTotal) is True:
        print("You have lost")
        return
    hs = input("Would you like to hit or stand? (1,2) 1 for hit, 2 to stand")
    if hs == "1":

        newCard = get_card()

        print("You got a {}".format(cards[newCard]))
        if newCard == 1 or newCard == 11:
            choice = input("Would You like the Ace to count as 1 or 11 (1, 11)")
            if choice == "1":
                userTotal += 1
                print(userTotal)
                cardlist.append(cards[newCard])
                user(userTotal, cardlist)
            else:
                userTotal += 11
                print(userTotal)
                cardlist.append(cards[newCard])
                user(userTotal, cardlist)


        else:
            userTotal = userTotal + newCard
            cardlist.append(cards[newCard])
            user(userTotal, cardlist)
        check(userTotal)
    elif hs == "2":
        print("Wait for dealer")
        cpuCard1 = get_card_dealer()
        cpuCard2 = get_card_dealer()
        cpuTotal = card1 + card2
        cpuCardlist = [cards[card1], cards[card2]]
        dealer(cpuCardlist, cpuTotal, userTotal)
    else:
        user(userTotal, cardlist)


def dealerMath(cpuTotal):
    difference = 21 - cpuTotal
    c = 0
    for i in deck:
        if i <= int(difference):
            c += 1
    length = len(deck)
    percentage = c/length
    if percentage >= .5:
        card = get_card_dealer()
        cpuTotal += card
        if check(cpuTotal) is True:
            print("Dealer Has Lost. You Have won.")
            return cpuTotal
        dealerMath(cpuTotal)
    else:
        print("Dealer does not draw...")
        return cpuTotal
    return cpuTotal


def dealer(cpuCardlist, cpuTotal, userTotal):
    print("Dealer has a ", cpuCard1)
    cpoo = dealerMath(cpuTotal)
    dist1 = (21 - cpoo)
    dist2 = (21 - userTotal)
    if dist1 < dist2:
        print("You lose...Dealer had a ",cpuTotal)
    elif dist2 < dist1:
        print("You win!")
    else:
        print("Draw...")
    print("The dealer has a total of ",cpuTotal)



def play_blackjack():
    print ("Welcome to Blackjack!")

    userTotal = card1 + card2
    user(userTotal, cardlist)


play_blackjack()
play_blackjack()
play_blackjack()
