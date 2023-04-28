'''LastStand'''
def main():
    '''LastStand'''
    digits = input()
    digits = digits.replace("[", "")
    digits = digits.replace("]", "")
    digits = digits.split(",")
    for i in digits:
        print(i[-1])
main()
