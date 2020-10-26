def countRange(list, x, y):
    count = 0
    for e in list:

        if x <= e and e < y:
            count = count + 1

    return count

def main():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(countRange(list, 2, 8))
    print(countRange(list, 11, 31))
    print(countRange(list, -1, 55))

    list = [1, 2, 3, 4, 1, 2, 3, 4]
    print( countRange(list, 1, 3))

main()