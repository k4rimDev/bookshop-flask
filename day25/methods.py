from ast import keyword
import pymysql.cursors


# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='12345',
                             database='Book',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


class Book:
    def create_table():
        with connection:
            with connection.cursor() as cursor:
                sql = """
                    CREATE TABLE Book_info(
                        id int unsigned auto_increment primary key,
                        title varchar(255) not null,
                        author varchar(100) not null,
                        published_at datetime DEFAULT CURRENT_TIMESTAMP,
                        exist boolean default true,
                        genre varchar(100),
                        price decimal(6,2) default 10.00
                    );
                """
                cursor.execute(sql)
            connection.commit()


    def create_book(title, author, genre, exists, price):
        with connection:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO Book_info (title, author, genre, exist, price) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (title, author, genre, exists, price))
            connection.commit()


    def show_all():
        with connection:
            with connection.cursor() as cursor:
                sql = """
                    SELECT * FROM Book_info
                """
                cursor.execute(sql)
                books = cursor.fetchall()
                return books


    def show_book(id):
        with connection:
            with connection.cursor() as cursor:
                sql = """
                    SELECT * FROM Book_info 
                    WHERE id = %s
                """
                cursor.execute(sql, id)
                book = cursor.fetchone()
                return book



    def change_status(exists, id):
        with connection:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE Book_info
                    SET exist = %s
                    WHERE id = %s
                """
                cursor.execute(sql, (exists, id))
                print("Updated succesfully!")
            connection.commit()


        
    def change_price(price, id):
        with connection:
            with connection.cursor() as cursor:
                sql = """
                    UPDATE Book_info 
                    SET price = %s
                    WHERE id = %s
                """
                cursor.execute(sql, (price, id))
                print("Updated succesfully!")
            connection.commit()


    def remove(id):
        with connection:
            with connection.cursor() as cursor:
                sql = """
                    DELETE FROM Book_info 
                    WHERE id = %s
                """
                cursor.execute(sql, id)
                print("Book deleted succesfully")
            connection.commit()
        

    def search(title_keyword, author_keyword):
        with connection:
            with connection.cursor() as cursor:
                sql = """
                    SELECT * FROM Book_info
                    WHERE title LIKE %s OR
                          author LIKE %s
                """
                cursor.execute(sql, (title_keyword, author_keyword))
                books = cursor.fetchall()
                return books
