'''diamond'''
def main(length=int(input())):
    '''diamond'''
    for row in range(0, length):
        for col in range(0, length):
            if row == length//2 or row + col == length//2 or col - row == length//2 \
                or row - col == length//2 or col == length - row + (length//2) - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
