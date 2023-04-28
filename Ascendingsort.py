"""AscendingSort"""
def main():
    """AscendingSort"""
    lst = []
    for _ in range(5):
        num = int(input())
        lst += [num]
    hong = sorted(lst)
    for i in range(5):
        print(hong[i])
main()
