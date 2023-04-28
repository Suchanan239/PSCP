'''Diamond I'''
def main():
    '''Diamond I'''
    count_a = int(input())
    count_b = int(input())
    num = []
    total = []
    for _ in range(count_a):
        diamond = input().split()
        num.append(diamond)
    for i in range(count_b):
        cals = 0
        for j in num:
            cals += int(j[i])
        total.append(cals)
    print(max(total))
main()
