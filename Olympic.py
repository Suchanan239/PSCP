'''Olympic'''
def main():
    '''Olympic'''
    country = dict()
    for _ in range(int(input())):
        score = input().split(" ")
        country[score[0]] = tuple(map(int, score[1:]))
    sort_country = sorted(country.items(), key=lambda a: sum(a[1]), reverse=True)
    sort_country.sort(key=lambda a: a[0])
    sort_country.sort(key=lambda a: a[1], reverse=True)
    tier = 0
    new = 0
    old = 0
    for country, score in sort_country:
        score_sum = sum(score)
        score = " ".join(map(str, score))
        if score != old:
            tier += new
            new = 0
            tier += 1
        elif tier != 0:
            new += 1
        print(tier, country, score, score_sum)
        old = score
main()
