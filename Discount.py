'''Discount'''
def main():
    '''Discount'''
    books = []
    while True:
        price = input()
        if price == "ENTER":
            break
        books.append(int(price))
    books.sort()
    if len(books) < 20:
        free_books = min(2, len(books)//6)
    else:
        free_books = len(books)//5
    print(sum(books[free_books:]))
main()
