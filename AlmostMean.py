"""AlmostMean"""
def main():
    """AlmostMean"""
    score = []
    data = []
    mean = 0
    value = 0
    count = int(input())
    for _ in range(count):
        text = input()
        data.append(text)
        text = text.split("\t")
        score.append(float(text.pop(1)))
    mean = (sum(score))/count
    mean_score = sorted(score)
    mean_score.reverse()
    for i in mean_score:
        if i <= mean:
            value = score.index(i)
            print(data[value])
            return
main()
