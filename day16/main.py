import sys
from datetime import datetime 
arr_book = " ".join(sys.argv[1:]).split("-")

date = datetime.today().strftime('%d %B %Y')

if len(arr_book) < 2:
    print('Wrong input')
    
else:
    book_name = arr_book[0]
    author_name = arr_book[1]

    if arr_book[0] == '' or arr_book[1] == '':
        print('Wrong input')

    else:
        print("Book name: ", book_name)

        print("Writer: ", author_name)

        print("Added in: ", date)