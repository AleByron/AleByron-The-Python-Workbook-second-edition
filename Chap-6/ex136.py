def reverseLookup(dic,val):
    value = []
    for k in dic:
        if dic[k]==val:
            value.append(k)

    return value


def main():
    dic1={'Name':'Alessandro', 'Age': 26, 'City': 'Milan'}
    dic2 = {'Yes, i\'m a ponitless 26': 26}
    dic3 = {}
    res = reverseLookup(dic1, 26)
    print(res)
if __name__ == "__main__":
        main()