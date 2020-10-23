def goodpass(x):
    score = 0
    res = False
    if len(x)>=8:
        for a in x:
            if 'a' <= a <= 'z':
                score = 1
                for a in x:
                    if 'A' <= a <='Z':
                        score=2
                        for a in x:
                            if '0' <= a <= '9':
                                score=3
                            else:
                                score= score
                    else:
                        score = score
            else:
                score = score

    if score==3:
        res = True
    else:
        res = False

    return res

def main():
    password = str(input('Enter a password:'))
    print(goodpass(password))

if __name__ == "__main__":
        main()
