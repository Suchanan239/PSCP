'''Coke'''
def main():
    '''Coke'''
    pricebefore = int(input())
    promotion = int(input())
    newprice = int(input())
    bottles = int(input())
    price = pricebefore
    caps = 0
    currently = 0
    while bottles > 0:
        caps += 1
        currently += price
        price = pricebefore
        if promotion == 0:
            currently = pricebefore*bottles
            break
        elif caps == promotion:
            price = newprice
            caps = 0
        bottles -= 1
    print(currently)
main()
