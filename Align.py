'''Align'''
def main():
    '''Align'''
    size = int(input())
    align = input()
    message = input()
    spacefor = size-len(message)
    if spacefor == 0:
        print(message)
    elif align == 'center':
        if spacefor % 2 > 0:
            spaceleft = spacefor % 2
            spaceleft += spacefor // 2
            spaceright = spacefor // 2
            print(spaceleft*' '+message+spaceright*' ')
        elif spacefor % 2 == 0:
            spaceleft = spacefor // 2
            spaceright = spacefor // 2
            print(spaceleft*' '+message+spaceright*' ')
    elif align == 'left':
        print(message+spacefor*' ')
    elif align == 'right':
        print(spacefor*' '+message)
main()
