import requests
import sys

book_names = sys.argv[2:]
book_name = ' '.join(book_names)

response_book = requests.get(f'https://www.omdbapi.com/?t={book_name}&apikey=49ffab34')

response_json = response_book.json()
response = response_json['Response']

if response == 'True':
    print('Title: ', response_json['Title'])
    print('Year: ', response_json['Year'])
    print('Released: ', response_json['Released'])
    print('Genre: ', response_json['Genre'])
    print('Director: ', response_json['Director'])
else:
    print('The movie has not been found.')

