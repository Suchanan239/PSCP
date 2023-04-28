'''Sequence N'''
def main():
    '''Sequence N'''
    mmm = int(input())
    if mmm >= 4:
        for row in range(mmm):
            for col in range(mmm):
                if col == 0 or col == mmm - 1 or (row == col):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
main()
