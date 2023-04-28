'''Bill'''
def main():
    '''Bill'''
    fad = int(input())
    service = (10/100)*fad
    if service < 50:
        service = 50
    if service > 1000:
        service = 1000
    if service >= 50 and service <= 1000:
        total = fad+service
        vat = (7/100)*total
        overall = total+vat
        print("%.2f" %overall)
main()
