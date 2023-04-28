'''temperature'''
def main(temp=float(input()), temp_unit1=input(), temp_unit2=input()):
    '''temperature'''
    if temp_unit1 == 'K':
        temp = temp-273.15
    elif temp_unit1 == 'F':
        temp = (temp-32)*(5/9)
    elif temp_unit1 == 'R':
        temp = (temp-491.67)*(5/9)
    else:
        temp = temp
    if temp_unit2 == 'K':
        temp = temp+273.15
    elif temp_unit2 == 'F':
        temp = (temp*(9/5))+32
    elif temp_unit2 == 'R':
        temp = (temp*(9/5))+491.67
    else:
        temp = temp
    print("%.2f" % temp)
main()
