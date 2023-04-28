'''Filter'''
import json
def main():
    '''Filter'''
    num = input()
    filter_1 = ['0']
    score = float(input())
    num = json.loads(num)
    for key in num:
        if num[key] >= score:
            filter_1.append('%s %.2f' %(key, float(num[key])))
        else:
            pass
    if len(filter_1) >= 2:
        filter_1.remove('0')
    filter_1.sort()
    for i in filter_1:
        if i == "0":
            print("Nope")
            break
        else:
            print("%s\t%.2f" %(i[0:8], float(i[9::])))
main()
