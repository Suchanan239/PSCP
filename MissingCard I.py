'''MissingCard I'''
def main():
    '''MissingCard I'''
    alp = ["A", "K", "Q", "J", "10", "9", "8",\
         "7", "6", "5", "4", "3", "2"]
    card = []
    for i in alp:
        spade = i + "S"
        heart = i + "H"
        diamond = i + "D"
        club = i + "C"
        card.append(spade)
        card.append(heart)
        card.append(diamond)
        card.append(club)
    for _ in range(51):
        missingcard = str(input())
        if missingcard in card:
            card.remove(missingcard)
    print(card[0])
main()
