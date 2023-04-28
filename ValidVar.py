'''ValidVar'''
def main(num=int(input())):
    '''ValidVar'''
    for _ in range(1, num+1):
        name = input()
        if name.isidentifier() == True and name != "if" and name != "else" and name != "while"\
            and name != "for" and name != "True" and name != "False" and name != "continue"\
                and name != "break" and name != "return" and name != "is" and name != "in"\
                    and name != "and" and name != "or" and name != "from" and name != "as"\
                        and name != "pass" and name != "not" and name != "def" and name != "None"\
                            and name != "elif":
            print("Valid")
        else:
            print("Invalid")
main()
