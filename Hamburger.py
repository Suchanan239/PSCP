'''Hamburger'''
def main():
    '''Hamburger'''
    left = int(input())
    right = int(input())
    middle = (left+right)*2
    if left > 0 and right > 0:
        print(("|"*left)+("*"*middle)+("|"*right))
main()
