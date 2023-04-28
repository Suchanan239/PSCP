'''Pringles'''
def main():
    '''Pringles'''
    top = input()
    snacks = input()
    botoom = input()
    length = int(input())
    count = 0
    result = 0
    eat = snacks[:length:]
    left = snacks[length::]
    for i in eat:
        if i == ")":
            count = count + 1
    for i in left:
        if i == ")":
            result = result + 1
    print(count)
    if result == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(top)
    print("%s%s" %((" "*length), snacks[length:]))
    print(botoom)
main()
