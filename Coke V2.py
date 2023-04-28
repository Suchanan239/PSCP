'''Coke V2'''
def main(pricebefore=int(input()), promotion=int(input()), \
    newprice=int(input()), bottles=int(input())):
    '''Coke V2'''
    if promotion == 0:
        print(pricebefore*bottles)
        quit()
    if bottles == 0:
        print(0)
        quit()
    howmany = bottles-1
    loop_count = howmany//promotion
    howmany_left = howmany%promotion
    price2loop = (pricebefore*(promotion-1))+newprice
    total = pricebefore+(loop_count*price2loop)+\
        (howmany_left*pricebefore)
    print(total)
main()
