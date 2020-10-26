from ex125 import createDeck
from ex125 import shuffle

hands = 4
n_cards = 13
listh = [] #hand for players
rem_deck = [] #cards that remains into the deck
deck = createDeck()
deck = shuffle(deck)
n = 0 #number of turns
x = len(deck)
while n_cards <= x:
    x = x - hands*n_cards
    n = n + 1
    if x < hands*n_cards:
        break


list_of_hands = [] #list of hands
for i in range(hands*n):
    new_list = []
    for j in range(0):
        new_list.append()
    list_of_hands.append(new_list)

y = 0
for i in range (n):
    for a in range (n_cards):
        for b in range (hands):
            if len(deck)<a:
                list_of_hands[b + y].append(deck[0])
                deck.pop(0)
            else:
                print(deck[0])
                list_of_hands[b+y].append(deck[a-1])

                deck.pop(a-1)

    y = y+hands

print(list_of_hands)
print(deck)

