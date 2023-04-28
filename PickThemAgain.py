'''PickThemAgain'''
def main():
    '''PickThemAgain'''
    sen = []
    text = input().split(" ")
    value = False
    for i in range(len(text)):
        value_new = int(text[i])
        if value_new % 3 == 0 or value_new % 5 == 0:
            sen.append(int(text[i]))
            value = True
    sen.reverse()
    if value:
        print(*sen, sep="\n")
    else:
        print("Nope")
main()
