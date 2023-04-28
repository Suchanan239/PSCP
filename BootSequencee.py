'''BootSequence'''
def main():
    '''BootSequence'''
    num = int(input())
    sss = ""
    for num in range(1, num+1):
        sss += str(num) + "_"
    sss = sss[:-1]
    print(sss)
main()
