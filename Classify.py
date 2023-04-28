'''Classify'''
def main():
    '''Classify'''
    collegian = []
    oldyear = 0
    while True:
        num = input()
        if num == 'END':
            break
        collegian.append(num[:4])
    for i in sorted(set(collegian)):
        year = i[:2]
        print(year if year != oldyear else "--", int(i[2:4]), collegian.count(i))
        oldyear = year
main()
