'''Future Message'''
def main():
    '''Future Message'''
    enter = input()
    if enter.isdigit():
        print("Number")
    elif enter.islower():
        print("Lowercase")
    elif enter.isupper():
        print("Uppercase")
    elif enter.istitle():
        print("Title")
    elif enter.isspace():
        print("Space")
    else:
        print("Other")
main()
