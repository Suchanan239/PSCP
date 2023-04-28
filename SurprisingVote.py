"""SurprisingVote"""
def main():
    """SurprisingVote"""
    overall = float(input())
    highest = float(input())
    last = 0
    if (highest*2) < overall:
        last = overall - (highest*2)
    if (highest - last) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
