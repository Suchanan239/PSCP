'''count'''
def main():
    '''count'''
    num = abs(int(input()))
    count = 1
    while num//10 > 0:
        count += 1
        num = int(num/10)
    print(count)
main()
    