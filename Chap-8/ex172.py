import sys

if len(sys.argv) < 2:
    print("Error in searching your checker file, no argument provided, the program will quit.")
    quit()

try:
    inf = open(sys.argv[1],'r')
    file = inf.read()
    file = file.split()
    v_words= []
    for word in file:
        c_word = ''
        copy = word
        for letter in word:
            if letter != 'a' and letter != 'e' and letter !='i' and letter!='o' and letter !='u' and letter !='y' :
                pass
            else:
                c_word = c_word + letter
                if c_word == 'aeiouy':
                    v_words.append(copy)
    print(v_words)

except FileNotFoundError:
    print('Something went wrong with your check file, the program wil quit')
    quit()

