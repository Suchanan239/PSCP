'''PhoneNumber'''
def main():
    '''PhoneNumber'''
    phone = input()
    options = input()
    if options == 'International':
        phone = '+66' + phone[1:]
    print(phone[:-8], phone[-8:-4], phone[-4:])
main()
