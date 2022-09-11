from methods import Book as db
import sys

command = sys.argv[1:]


# Add commands
if command[0] == 'add':
    if command[1] == 'table':
        db.create_table()
    elif command[1] == 'book':
        title = input("Enter title of a book: ")
        author = input("Enter author of a book: ")
        exists = int(input("Enter exists of a book (If exists write 1 else 0): "))
        genre = input("Enter genre of a book: ")
        price = int(input("Enter price of a book: "))

        db.create_book(title, author, genre, exists, price)

    else:
        print("Error!")


# Show commands
elif command[0] == 'show':
    if command[1] == 'all':
        books = db.show_all()
        for book in books:
            print(book)

    elif command[1] == 'book':
        id = int(input("Enter a id of book: "))
        book = db.show_book(id)
        print(book)

    else: 
        print("Error!")

# Change commands
elif command[0] == 'change':
    if command[1] == 'status':
        id = int(input("Enter id of book: "))
        exists = int(input("Enter new status (1 or 0): "))
        db.change_status(exists, id)

    elif command[1] == 'price':
        id = int(input("Enter id of book: "))
        price = int(input("Enter new price: "))
        db.change_price(price, id)

    else: 
        print("Error!")


# Remove command
elif command[0] == 'remove' and len(command) == 1:
    id = int(input("Enter id of a book that you want remove: "))
    db.remove(id)


# Search command 
elif command[0] == 'search' and len(command) == 1:
    keyword = input("Enter a keyword: ")
    keyword = '%{}%'.format(keyword)
    books = db.search(keyword, keyword)

    if len(books) < 1:
        print("No book found!")
    else:
        for book in books:
            print(book)

else:
    print("Error!")

