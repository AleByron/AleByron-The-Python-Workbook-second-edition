import random
def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    tot = dice1 + dice2

    return tot

def main():
    x = 0

    dict = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
    perc = {'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}
    exp_p = [2.78,5.56,8.33,11.11,13.89,16.67,13.89,11.11,8.33,5.56,2.78]
    while x <=1000:
        a = str(roll())
        if a in dict:
            dict[a]= dict[a]+1
        x = x+1

    for k in perc:
        perc[k] = dict[k]/10

    x = 0
    print("{0:<10} {1:<20} {2:<20}".format('Total', 'Simulated percent', 'Expected percent'))
    for i in range (2,13):
        i = str(i)
        print("{0:<10} {1:<20} {2:<20}".format(dict[i], perc[i], exp_p[x]))
        x = x+1



main()