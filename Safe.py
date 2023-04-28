'''Safe'''
def rotatedown(password, lockpass):
    """Safe"""
    down = 0
    while lockpass != password:
        if lockpass >= 25:
            lockpass = -1
        down += 1
        lockpass += 1
    return down
def rotateup(password, lockpass):
    """Safe"""
    upp = 0
    while lockpass != password:
        if lockpass <= 0:
            lockpass = 26
        upp += 1
        lockpass -= 1
    return upp
def main(correct, lock):
    """Safe"""
    count = 0
    for i in range(len(correct)):
        password = ord(correct[i])-65
        lockpass = ord(lock[i])-65
        if password != lockpass:
            down = rotatedown(password, lockpass)
            upp = rotateup(password, lockpass)
            if upp <= down:
                count += upp
            elif down < upp:
                count += down
    print(count)
main(input().upper(), input().upper())
