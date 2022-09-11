import sys
import os
from datetime import datetime
from os.path import exists

if not os.path.isdir('books'):
    os.mkdir('books')
    os.chdir('books')
else:
    os.chdir('books')

# Get Input
commands = sys.argv

def no_book(func):

    def inner(book_arr):

        func(book_arr)
        count_book = len(book_arr)
        if count_book > 1:
            print(f'There are {count_book} books\n')
        else:
            print(f'There is {count_book} book\n')

        for book in book_arr:
            for data in book.split(' || '):
                print(data)
    return inner


@no_book
def show_all(book_list):
    return len(book_list)
    

def add_book(title, author, add_date):
    # Read file for get count of lines 
    if not(exists('id_list.txt')):
        with open('id_list.txt', 'w') as id_list:
            id_list.write('1')  
            id = 1          
    else:
        with open('id_list.txt', 'r+') as id_list:
            id = int(id_list.readline().strip()) + 1
            id_list.seek(0)
            id_list.write(f'{id}')
        
    # Append data to file
    with open('book_list.txt', 'a') as book_list:
        book_id = id
        book_list.write(f'Book Id: {book_id} || ')
        book_list.write(f'Book name: {title} || ')
        book_list.write(f'Writer: {author} || ')
        book_list.write(f'Added in: {add_date} || ')
        book_list.write('******************************\n')

def show_book(book_id):
    try:
        with open('book_list.txt', 'r') as book_list:
            book_str = f'Book Id: {book_id} '
            for line in book_list.readlines():
                    if book_str in line:
                        for data in line.split(' || '):
                            print(data)
    except:
        print('Error!')

def remove_book(book_id):
    try:
        with open('book_list.txt', 'r+') as book_list:
            book_str = f'Book Id: {book_id} '
            # has_book = False
            for i, line in enumerate(book_list.readlines()):
                
                if i == 0:
                    book_list.seek(0)
                    book_list.truncate()
                if not book_str in line:
                    book_list.write(line)

            if not book_str in line:
                print('There is no book')
            else:
                print("Deleted succesfully!")
    except:
        print("Error!!")
        

if commands[1] == 'add':
    title = input('Enter book name:\n')
    print("\n")
    author = input('Enter writer name:\n')
    print("\n")
    print("Added succesfully!")
    add_date = datetime.today().strftime('%d %B %Y')

    add_book(title, author, add_date)

elif commands[1] == 'remove':
    book_id = input('Enter book ID:\n')
    print("\n")
    remove_book(book_id)

elif len(commands) > 2:
        if commands[2] == 'all':
            if os.path.exists('book_list.txt'):
                with open('book_list.txt', 'r+') as book_list:
                    book_arr = book_list.readlines()
                    show_all(book_arr)
            else:
                print('Error!')
        else:
            print("Wrong input!")

elif commands[1] == 'show':
    book_id = input('Enter book ID:\n')
    show_book(book_id)

else:
    print("Wrong input!")