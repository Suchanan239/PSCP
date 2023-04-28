'''Calculator V2'''
def main():
    '''Calculator V2.py'''
    num = int(input())
    count = len(str(num))
    count_1 = 1
    count_9 = 9
    tap = 0
    if num == 1:
        print(1)
        quit()
    for i in range(1, count):
        times = (count_9-count_1)+1
        tap += times*i
        count_1 = int(str(count_1)+"0")
        count_9 = int(str(count_9)+"9")
    finish = ((num - count_1)+1)*count
    total = (tap + finish)+num
    print(total)
main()
