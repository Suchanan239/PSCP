'''Matrix_MN'''
def main(row=int(input()), col=int(input())):
    '''Matrix_MN'''
    list_n = []
    for _ in range(row*col):
        list_n.append(int(input()))
    for i in range(row):
        for k in range(col):
            print(list_n[i*col+k], end=" ")
        print()
main()
