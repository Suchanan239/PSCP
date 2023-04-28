'''Parallelogram'''
def main():
    '''Parallelogram'''
    phase = input()
    combine = ''
    for char in phase:
        combine += char
        print(' '*(len(phase)-len(combine))+combine)
    for i in range(len(phase)):
        if i == 0:
            continue
        combine = phase[0+i:len(phase)]
        print(combine+' '*(len(combine)-i))
main()
