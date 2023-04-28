"""count"""
def main():
    """count"""
    nnn = abs(int(input()))
    ccc = 0
    if nnn > 0:
        while nnn > 0:
            ccc = (ccc)+1
            nnn = nnn//10
        print(ccc)
    elif nnn == 0:
        print(1)
main()
