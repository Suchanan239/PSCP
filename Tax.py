'''Tax'''
def main(years=int(input()), cc_unit_of_car=int(input())):
    '''Tax'''
    if cc_unit_of_car <= 600:
        tax = cc_unit_of_car*0.5
    elif cc_unit_of_car <= 1800 and cc_unit_of_car > 600:
        tax = ((cc_unit_of_car-600)*1.50)+300
    elif cc_unit_of_car > 1800:
        tax = ((cc_unit_of_car-1800)*4)+2100
    if years == 6:
        print("%.2f" %(tax*0.9))
    elif years == 7:
        print("%.2f" %(tax*0.8))
    elif years == 8:
        print("%.2f" %(tax*0.7))
    elif years == 9:
        print("%.2f" %(tax*0.6))
    elif years >= 10:
        print("%.2f" %(tax*0.5))
    if years < 6:
        print("%.2f" %tax)
main()
