'''Kangaroo'''
def main(kangaroo=[int(input()) for _ in range(3)]):
    '''Kangaroo'''
    print(max(kangaroo[2]-kangaroo[1], kangaroo[1]-kangaroo[0])-1)
main()
