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

class Books():
    title = ''
    author = ''
    id = 0
    date = ''

    def set_id(self):
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
        
        return id

    def set_date(self):
        add_date = datetime.today().strftime('%d %B %Y')
        return add_date
    
    # Add book method
    def add_book(self, title, author): 
        
        # Append data to file
        with open('book_list.txt', 'a') as book_list:
            book_id = self.set_id()
            book_list.write(f'Book Id: {book_id} || ')
            book_list.write(f'Book name: {title} || ')
            book_list.write(f'Writer: {author} || ')
            book_list.write(f'Added in: {self.set_date()} || ')
            book_list.write('******************************\n')


    # Show book method
    def show_book(self, book_id):
        try:
            with open('book_list.txt', 'r') as book_list:
                book_str = f'Book Id: {book_id} '
                book_arr = book_list.readlines()
                has_book = False
                for line in book_arr:
                    if len(book_arr) == 0:
                        print("There is no book")
                    elif book_str in line:
                        for data in line.split(' || '):
                            has_book = True
                            print(data)
                if not has_book:
                    print("There is no book")
        except:
            print('Error!')

    # Remove book method
    def remove_book(self, book_id):
        try:
            with open('book_list.txt', 'r+') as book_list:
                book_str = f'Book Id: {book_id} '
                has_book = False
                book_arr = book_list.readlines()

                for linex in book_arr:
                    if book_str in linex:
                        has_book = True

                for i, line in enumerate(book_arr):
                    if i == 0:
                        book_list.seek(0)
                        book_list.truncate()
                    if not book_str in line:
                        book_list.write(line)

                if has_book:
                    print("Deleted succesfully!")
                else:
                    print('There is no book')
                
        except:
            print('There is no book')

    
    # Show all method
    def show_all(book_arr):
        with open('book_list.txt', 'r+') as book_list:
            book_arr = book_list.readlines()
            count_book = len(book_arr)

            if count_book > 1:
                print(f'There are {count_book} books\n')
            else:
                print(f'There is {count_book} book\n')

            for book in book_arr:
                for data in book.split(' || '):
                    print(data)


# Get commands

if commands[1] == 'add':
    title = input('Enter book name:\n')
    print("\n")
    author = input('Enter writer name:\n')
    print("\n")
    print("Added succesfully!")
    
    book = Books()

    book.add_book(title, author)

elif commands[1] == 'remove': 
    book_id = input('Enter book ID:\n')
    print("\n")
    book = Books()
    book.remove_book(book_id)

elif len(commands) > 2:
        if commands[2] == 'all':
            book = Books()
            if os.path.exists('book_list.txt'):
                book.show_all()
            else:
                print('Error!')
        else:
            print("Wrong input!")

elif commands[1] == 'show':
    book = Books()
    book_id = input('Enter book ID:\n')
    book.show_book(book_id)

else:
    print("Wrong input!")