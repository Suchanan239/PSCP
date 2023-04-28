"""PickThem"""
import json
def main():
    """Pickthem"""
    num = input()
    number = json.loads(num)
    count = 0
    for i in number:
        if i % 2 == 0:
            count += 1
            print(i)
    if count == 0:
        print("Nope")
main()
