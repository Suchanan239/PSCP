"""MissingNumber"""
def main():
    """MissingNumber"""
    num = int(input())
    numbet = []
    while True:
        num_1 = int(input())
        if num_1 == 0:
            break
        numbet.append(num_1)
    for i in range(1, num + 1):
        if i not in numbet:
            print(i)
main()
