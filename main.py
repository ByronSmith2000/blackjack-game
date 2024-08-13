from random import choice
from card import Card

ace = Card("Ace", 11)
two = Card("Two", 2)
three = Card("Three", 3)
four = Card("Four", 4)
five = Card("Five", 5)
six = Card("Six", 6)
seven = Card("Seven", 7)
eight = Card("Eight", 8)
nine = Card("Nine", 9)
ten = Card("Ten", 10)
jack = Card("Jack", 10)
queen = Card("Queen", 10)
king = Card("King", 10)


cards = [ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king]

player_hand = []
dealer_hand = []

def sum_of_hand(hand):
    sum = 0

    for card in hand:
        sum += card.get_values()

    return sum

if __name__ == '__main__':
    
    dealer_hand = [choice(cards), choice(cards)]
    #print(f"Dealer's first card is {dealer_hand[0]}")
    print(sum_of_hand(dealer_hand))



