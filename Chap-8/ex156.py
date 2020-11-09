line = input("Enter a number: ")
res = 0

while line != "":
    try:
        num = float(line)
        res = res + num
        print("Sum:", res)

    except ValueError:
        print("Not a number")
        line = input("Try again: ")
        num = float(line)
        res = res + num
        print("Sum:", res)
    line = input('Enter the next number:')

print('The final sum is:', res)