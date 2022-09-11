from flask import render_template, request
from app import app
from models import *



# Index page
@app.route('/', methods=['GET'])
def index():
    books = Book.query.all()

    return render_template('index.html', active='index', books=books)



# Product page
@app.route('/product', methods=['GET', 'POST'])
def product():
    book_list = [{
        'id': 1,
        'name': 'İncognito (beyinin gizli həyatı)',
        'description': 'Tanınmış nevroloq D.İqlmenin 20-dən çox dilə tərcümə edilən və indidən klassik əsərə çevrilən bu kitabı beynin sirli dünyasına təcrübələr, elmi biliklər və tarixi faktlar işığında səyahət edir. Kitab tibbi mövzuda olsa da, müəllif yazarlıq məharətini və zəngin biliyini birləşdirərək elmi faktları sadə və müqayisəli dillə oxucularına təqdim edir. Müəllif əsər boyu sədaqət geni, qumarbazlara çevrilən parkinson xəstələri, gen-mühit əlaqəsi, “yaxşı” və “pis” gen, şüuraltı və qərarvermə mexanizmi, məsuliyyət anlayışı, beynin insan həyatında rolu kimi bir çox mövzulara toxunur. Alim bu mövzuların beyinlə əlaqəsini izah etməklə kifayətlənmir, beyinlə bağlı müxtəlif formullar və modellər irəli sürür. İnsan psixologiyası və davranışlarına neyron və gen prizmasından baxmağı öyrədir. Elmi-populyar dildə yazılmış bu kitab xüsusən müəllimlər, psixoloqlar, valideynlər, həkimlər üçün mühüm bilikləri ehtiva edir.',
        'price': 15.00,
        'discount_price': 12.00,
        'image_path': 'images/Inkognito.png',
        'language': 'Azərbaycanca',
        'genre': 'Psixologiya',
        'author': 'David Eagleman',
        'publish': 'Qanun Nəşriyyatı',
        'count': 2
    }]

    if request.method == 'POST':
        _form = request.form
        name = _form['name']

        print(name)
    return render_template('product.html', book=book_list[0], active='product')



# Book detail page
@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.all()[book_id-1]
    language = Language.query.filter(Language.id.in_(db.select([Language_Book.language_id]).filter(Language_Book.book_id == book_id))).all()
    genre = Genre.query.filter(Genre.id.in_(db.select([Genre_Book.genre_id]).filter(Genre_Book.book_id == book_id))).all()


    return render_template('book.html', book=book, language=language, genre=genre)


