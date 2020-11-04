mess = input("Enter a string: ")
mess2 = input("Enter a string: ")

let = {}
let2 = {}
for x in mess:
    if x in let:
        let[x] = let[x]+1
    else:
        let[x] = 1

for x in mess2:
    if x in let2:
        let2[x] = let2[x]+1
    else:
        let2[x] = 1

if let == let2:
    print('It\'s an anagram')
else:
    print('It\'s not an anagram')
