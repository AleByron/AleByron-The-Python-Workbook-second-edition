
def rec():
    res = 0
    val = str(input('Enter an int:'))
    if val != '':
        val = int(val)
        res = val + rec()
        print(res)
    else:
        return res

    return res
def main():

    print(rec())


main()
