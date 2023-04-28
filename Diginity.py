'''Diginity'''
def main():
    '''Diginity'''
    num = 0
    while True:
        password = int(input())
        if password == 0:
            break
        else:
            for i in str(password):
                if len(str(num)) == 1:
                    print(num)
                else:
                    while len(num) > 1:
                        num += int(i)
main()
