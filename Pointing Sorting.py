"""Point Sorting"""
def main():
    '''Pointing'''
    pnt = int(input())
    lst = []
    for _ in range(pnt):
        num = int(input())
        for _ in range(num):
            val = input().split()
            lst.append(val)
            lst.sort(key=lambda x: int(x[1]), \
                reverse=True)
            lst.sort(key=lambda x: \
                int(x[0])+int(x[1]))
        for i in lst:
            print(*i)
        lst.clear()
main()
