'''Parity'''
def main():
    '''Parity'''
    bits = input()
    options = input()
    num = 0
    for i in bits:
        if i == '0':
            num += 0
        elif i == '1':
            num += 1
    if num%2 == 0 and options == "Even":
        newbits = bits+'0'
    elif num%2 == 0 and options == "Odd":
        newbits = bits+'1'
    elif num%2 != 0 and options == "Even":
        newbits = bits+'1'
    elif num%2 != 0 and options == "Odd":
        newbits = bits+'0'
    print(newbits)
main()
