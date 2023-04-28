'''Calculator'''
def main():
    '''Calculator'''
    num = int(input())
    count = 0
    if num == 1:
        print("1")
    else:
        for i in range(1, num+1):
            count += len(str(i))
        print(num+count)
main()
