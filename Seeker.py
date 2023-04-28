'''Seeker'''
def main():
    '''Seeker'''
    string = input()
    check = ""
    count = 0
    for i in string:
        if i.isdigit() == True:
            check += i
        else:
            if check == "":
                count += 0
            else:
                count += int(check)
                check = ""
    if check.isdigit() == True:
        print(count + int(check))
    else:
        print(count)
main()
