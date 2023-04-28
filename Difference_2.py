'''Difference'''
import json
def main():
    '''Difference'''
    list1 = json.loads(input())
    list2 = json.loads(input())
    set1 = set(list1)
    set2 = set(list2)
    check = set1.union(set2)
    count = 0
    for i in sorted(check):
        if abs(list1.count(i)-list2.count(i)) != 0:
            print(i, abs(list1.count(i)-list2.count(i)))
            count += 1
    if count == 0:
        print("ONAJI DAYO!")
main()
