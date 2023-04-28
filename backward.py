"""backward"""
def main():
    """backward"""
    lst = []
    while True:
        txt = input()
        if txt == 'NULL':
            break
        lst.append(txt)
    print(*lst[-1::-1], sep='\n')
main()
