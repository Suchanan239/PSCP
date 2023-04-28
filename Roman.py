'''Roman'''
def main(roman_input=input()):
    '''Roman'''
    roman = {"M": 1000, "D": 500, "C": 100, \
        "L": 50, "X": 10, "V": 5, "I": 1}
    num = 0
    for i, j in enumerate(roman_input):
        if (i+1) == len(roman_input) or \
            roman[j] >= roman[roman_input[i+1]]:
            num += roman[j]
        else:
            num -= roman[j]
    print(num)
main()
