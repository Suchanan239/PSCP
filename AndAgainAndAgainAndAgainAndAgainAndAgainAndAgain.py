'''AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain'''
def main():
    '''AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain'''
    sen = []
    val = input().replace(".", "")
    wrd = val.split()
    for ori in wrd:
        total = ori.count("a") + ori.count("e") +\
             ori.count("i") + ori.count("o") + ori.count("u")
        if total >= 2:
            sen.append(ori)
    if len(sen) == 0:
        sen.append("Nope")
    sen.sort()
    for ori in sen:
        print(ori)
main()
