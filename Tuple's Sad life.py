'''Tuple's Sad life'''
def main():
    '''Tuple's Sad life'''
    aaa = tuple(input().split(" "))
    index_a = input()
    for _ in range(aaa.count(index_a)):
        for _ in range(aaa.count(index_a)):
            print(int(aaa.index(index_a)), end=" ")
        print()
main()
