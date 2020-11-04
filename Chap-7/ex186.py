def compress(file):

    if len(file) == 0:
        return []
    else:
        x = 1

        while x < len(file) and file[x] == file[x - 1]:
            x = x + 1

        res = [file[0], x] + compress(file[x : len(file)])

    return res

def main():

    s = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B']

    print(compress(s))

main()