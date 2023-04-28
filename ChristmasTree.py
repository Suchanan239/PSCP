'''ChristmasTree'''
def main():
    '''ChristmasTree'''
    leaves = int(input())
    base = int(input())
    if leaves%2 != 0:
        for i in range(leaves):
            print(" "*(leaves-i-1) + "*"*(2*i+1))
        for i in range(base):
            print(" "*(leaves-2) + "---")
main()
