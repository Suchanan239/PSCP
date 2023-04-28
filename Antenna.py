'''Antenna'''
import json
def main(radius=int(input())):
    '''Antenna'''
    pos_of_people = sorted(json.loads(input()))
    limit = 0
    count = 1
    if not pos_of_people:
        return print("0")
    limit = pos_of_people.pop(0)+(radius*2)
    while pos_of_people:
        new_pos_of_people = pos_of_people.pop(0)
        if new_pos_of_people > limit:
            count += 1
            limit = new_pos_of_people+radius*2
    print(count)
main()
