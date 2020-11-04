def decoding(compressed):
    if compressed ==[]:
        x = ''
    else:
        y = compressed[0]
        z = compressed[1]
        x =  int(z)*y + decoding(compressed[2:])

    return x

def main():
    li = ['A', 12, 'B', 4, 'A', 6, 'B', 3]
    li_fin = []
    decoded = decoding(li)
    for i in decoded:
        li_fin.append(i)
    print(li_fin)

if __name__ == "__main__":
        main()