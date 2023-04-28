'''RightArrow'''
def main():
    '''RightArrow'''
    width = int(input())
    height = int(input())
    space = int((height-1)/2)
    for i in range(0, space+1, +1):
        print((" "*abs(i))+("*")*width)
    for i in range(space-1, -1, -1):
        print((" "*abs(i))+("*")*width)
main()
