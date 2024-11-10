import random
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

my_cards = []
com_cards = []
for i in range(2):
    my_cards.append(random.choice(cards))
    com_cards.append(random.choice(cards))

def check_bj(a):
    if 11 in a:
        if sum(a) > 21:
            index = a.index(11)
            a[index] = 1
        if sum(a) == 21:
            return True
        else:
            return False
    else:
        if sum(a) == 21:
            return True
        else:
            return False

def bj(cards, card):
    if 11 in cards:
        if sum(cards) > 21:
            index = cards.index(11)
            cards[index] = 1
        if sum(cards) < 21:
            new = input("Type 'y' to get another card, type 'n' to pass: ")
            if new == "y":
                cards.append(random.choice(card))
                print(cards)
            else:
                print(cards)
    
    else:
        if sum(cards) < 21:
            new = input("Type 'y' to get another card, type 'n' to pass: ")
            if new == "y":
                cards.append(random.choice(card))
                print(cards)
            else:
                print(cards)
                

def com_bj(cards, card):
    if 11 in cards:
        if sum(cards) > 21:
            index = cards.index(11)
            cards[index] = 1
        if sum(cards) < 21:
            if sum(cards) < 16:
                cards.append(random.choice(card))
                print(cards)
            else:
                print(cards)
                
    else:
        if sum(cards) < 21:
            if sum(cards) < 16:
                cards.append(random.choice(card))
                print(cards)
            else:
                print(cards)

game = "w"
while game == "w":
    if check_bj(com_cards):
        print(f"My cards:  {my_cards}")
        print(f"computers cards:  {com_cards}")
        print("You lose, Computer have a BLACKJACK")
        break
    elif check_bj(my_cards):
        print(f"My cards:  {my_cards}")
        print(f"computers cards:  {com_cards}")
        print("You Won, You have a BLACKJACK")
        break
    else:
        print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"Computer's first card: {com_cards}")
        my_score = bj(my_cards, cards)
        com_score = com_bj(com_cards, cards)
        """if sum(my_score) > sum(com_score):
            print("W")
        elif sum(my_score) < sum(com_score):
            print("L")
        elif sum(my_score) == sum(com_score):
            print("D")
        else:
            print("fuck")"""
        print(my_score)
        print(com_score)
        break