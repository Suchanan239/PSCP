"""Iphone13"""
def iphone_check(iphone, stg):
    """Iphone13"""
    if stg == "128 GB":
        return 0
    elif stg == "256 GB":
        return 4000
    elif stg == "512 GB":
        return 12000
    elif stg == "1 TB":
        if iphone == "iPhone 13 mini" or iphone == "iPhone 13":
            return -1
        else:
            return 20000
    else:
        return -1

def main():
    """iphone"""
    ver = input()
    stg = input()
    stg = iphone_check(ver, stg)
    if stg == -1:
        print('Not Available')
    else:
        if ver == "iPhone 13 mini":
            print(25900 + stg)
        elif ver == "iPhone 13":
            print(29900 + stg)
        elif ver == "iPhone 13 Pro":
            print(38900 + stg)
        elif ver == "iPhone 13 Pro Max":
            print(42900 + stg)
        else:
            print('Not Available')
main()
