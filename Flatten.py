'''Flatten'''
import json
def main(val: list):
    '''Flatten'''
    num = []
    for ori in val:
        if isinstance(ori, list):
            num += main(ori)
        else:
            num.append(ori)
    num.sort(reverse=True)
    return num
print(main(json.loads(input())))
