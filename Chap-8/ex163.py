from ex117 import splitWords
def FreqNames(mess):
    try:
        inf = open('C:\\Users\\ale\\PycharmProjects\\WorkbookExercises\\Files\\Popular_Baby_Names.csv')

        yearsm = {}
        yearsf = {}
        for l in inf:
            line = inf.readline()
            arr = splitWords(line)
            if arr[0] not in yearsm and arr[1] == 'MALE':
                yearsm.setdefault(arr[0], [])
                yearsm[arr[0]].append(arr[len(arr) - 3])
            elif arr[0] in yearsm and arr[1] == 'MALE':
                yearsm[arr[0]].append(arr[len(arr) - 3])
            elif arr[0] not in yearsf and arr[1] == 'FEMALE':
                yearsf.setdefault(arr[0], [])
                yearsf[arr[0]].append(arr[len(arr) - 3])
            elif arr[0] in yearsf and arr[1] == 'FEMALE':
                yearsf[arr[0]].append(arr[len(arr) - 3])

    except FileNotFoundError:
        return print('Something went wrong, the program wil quit')

    return yearsm[mess], yearsf[mess]

def main():
    mess = input('Enter an year:')

    print('Most popular male names of your year are:', FreqNames(mess)[0])
    print('Most popular female names of your year are:', FreqNames(mess)[1])

if __name__ == "__main__":
        main()