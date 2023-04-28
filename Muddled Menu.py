"""Muddled Menu"""
def main():
    """Muddled Menu"""
    lst = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        elif menu == "SOMETHING'S WRONG":
            lst.clear()
        elif menu == "CLOSED":
            return print("Full Course: [] Reversed: []")
        elif menu[0:10:] == "Can't do: ":
            lst.remove(menu[10::])
        else:
            menu = menu.split(" #")
            if menu[1].isnumeric():
                lst.insert(int(menu[1])-1, menu[0])
            elif menu[1] == "N":
                lst.append(menu[0])
    print("Full Course: %s Reversed: %s" %(lst, lst[::-1]))
main()
