"""Bookworm"""
def main():
    """Bookworm"""
    count = int(input())
    for _ in range(count):
        mins = float(input())
        value = sorted([float(input()) for _ in range(int(input()))])
        i = 0
        for i in range(len(value)):
            if sum(value[:i+1]) > mins:
                break
            i += 1
        print(i)
main()
