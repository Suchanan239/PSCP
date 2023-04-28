'''One For All'''
def main():
    '''One For All'''
    num = int(input())
    names = ""
    for i in range(1, num+1):
        stu = input()
        if i%2 == 0:
            name = stu+"-"*i
        elif i%2 != 0:
            name = stu+"*"*i
        names += name
    overall = names[:-num]
    overall = overall+"_"+str(num)
    print(overall)
main()
