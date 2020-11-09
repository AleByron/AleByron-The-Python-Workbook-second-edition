from ex117 import splitWords
def FreqNamesTot():
    try:
        inf = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\Popular_Baby_Names.csv')

        yearsm = []
        yearsf = []
        for l in inf:
            line = inf.readline()
            line = line.upper()
            arr = splitWords(line)

            if arr[len(arr) - 3] not in yearsm and arr[1] == 'MALE':
                yearsm.append(arr[len(arr) - 3])
            if arr[len(arr) - 3] not in yearsf and arr[1] == 'FEMALE':
                yearsf.append(arr[len(arr) - 3])


    except FileNotFoundError:
        return print('Something went wrong, the program wil quit')

    return yearsm, yearsf

def main():

    print('Most popular male names are:', FreqNamesTot()[0])
    print('Most popular female names are:', FreqNamesTot()[1])

if __name__ == "__main__":
        main()