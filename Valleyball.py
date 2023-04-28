"""Volleyball"""
def main():
    """Valleyball"""
    data = input()
    a_score = 0
    b_score = 0
    sett = 1
    a_won = 0
    b_won = 0
    game_end = False
    for aaa in data:
        if aaa == "A":
            a_score += 1
        elif aaa == "B":
            b_score += 1
        if sett <= 4:
            if a_score >= 25 and a_score - b_score >= 2:
                print("Set %d: A (%d) | B (%d)"%(sett, a_score, b_score))
                sett += 1
                a_score = 0
                b_score = 0
                a_won += 1
            elif b_score >= 25 and b_score - a_score >= 2:
                print("Set %d: A (%d) | B (%d)"%(sett, a_score, b_score))
                sett += 1
                a_score = 0
                b_score = 0
                b_won += 1
        else:
            if a_score >= 15 and a_score - b_score >= 2:
                print("Set %d: A (%d) | B (%d)"%(sett, a_score, b_score))
                sett += 1
                a_score = 0
                b_score = 0
                a_won += 1
            elif b_score >= 15 and b_score - a_score >= 2:
                print("Set %d: A (%d) | B (%d)"%(sett, a_score, b_score))
                sett += 1
                a_score = 0
                b_score = 0
                b_won += 1
        if a_won == 3:
            game_end = True
            print("A won %d:%d set"%(a_won, b_won))
        elif b_won == 3:
            game_end = True
            print("B won %d:%d set"%(b_won, a_won))
    if game_end == False:
        print("Set %d: A (%d) | B (%d)"%(sett, a_score, b_score))
        print("The game has not finished yet.")
main()
