import random


def bingoCard():
    card = {'b': [], 'i': [], 'n': [], 'g': [], 'o': []}

    y = 0

    while y < 5:
        b = random.randint(1, 15)
        if b not in card['b']:
            card['b'].append(b)
            y = y + 1
    y = 0
    while y < 5:
        i = random.randint(16, 30)
        if i not in card['i']:
            card['i'].append(i)
            y = y + 1
    y = 0
    while y < 5:
        n = random.randint(31, 45)
        if n not in card['n']:
            card['n'].append(n)
            y = y + 1
    y = 0
    while y < 5:
        g = random.randint(46, 60)
        if g not in card['g']:
            card['g'].append(g)
            y = y + 1
    y = 0
    while y < 5:
        o = random.randint(61, 75)
        if o not in card['o']:
            card['o'].append(o)
            y = y + 1

    return card

def main():
    print(bingoCard())

if __name__ == "__main__":
    main()


