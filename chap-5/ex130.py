#
from ex129 import tk

def binary(tok):
    x = []

    for i in range(len(tok)):

        if i == 0 and (tok[i] == "+" or tok[i] == "-"):
            x.append("u" + tok[i])

        elif i>0 and (tok[i] == "+" or tok[i] == "-") and (tok[i-1] == "+" or tok[i-1] == "-" or tok[i-1] == "*" or tok[i-1] == "/" or tok[i-1] == "("):
            x.append("u" + tok[i])

        else:
            x.append(tok[i])

    return x

def main():

    exp = input("Enter a mathematical expression: ")
    tok = tk(exp)
    new_tok = binary(tok)
    print("With unary operators marked: ", new_tok)

if __name__ == "__main__":
    main()