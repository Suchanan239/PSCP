'''Palindrome'''
def main():
    '''Palindrome'''
    value_a = int(input())
    value_b = input()
    increase = 0
    while increase != value_a:
        value_c = "%02d" % (int(value_b[-2:]) + 1)
        hours = value_b[0:2].replace(":", "")
        if int(value_c) % 60 == 0 and int(value_c) != 0:
            value_c = "00"
            y_value = int(hours) + 1
            hours = str(y_value)
        if int(hours) % 24 == 0:
            hours = "0"
        value_b = hours + ":" + value_c
        if value_b.replace(":", "") == value_b.replace(":", "")[::-1]:
            increase = increase + 1
            print(value_b)
main()
