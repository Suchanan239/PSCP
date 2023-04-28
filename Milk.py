'''Milk'''
def main():
    '''Milk'''
    aaa = int(input())
    bbb = int(input())
    ccc = int(input())
    ddd = int(input())
    eee = ddd//aaa
    fff = eee
    while fff >= bbb and bbb > 0:
        ggg = (fff//bbb)*ccc
        hhh = fff%bbb
        eee += ggg
        fff = ggg+hhh
    print(eee)
main()
