'''LineSorting'''
def main():
    '''LineSorting'''
    count = int(input())
    total = []
    for _ in range(1, count+1):
        total.append(input())
    total = sorted(total, key=lambda x: (len(x), x))
    print(*total, sep="\n")
main()
