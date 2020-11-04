from itertools import combinations_with_replacement

def num_coins(amount, x, i=0):
    coins = [0.25, 0.10, 0.05, 0.01]
    comb = list(combinations_with_replacement(coins, x))
    if amount != round(sum(comb[i]), 4):
        i += 1
        if i >= len(list(comb)):
            return False
        else:
            return num_coins(amount, x, i)
    else:
        return True
def main():
    amount = float(input("Enter an amount of money: "))
    n_coins = int(input("Enter a number of coins: "))
    print(num_coins(amount, n_coins))

main()