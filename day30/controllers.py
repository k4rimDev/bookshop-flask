from datetime import datetime
from werkzeug.security import check_password_hash
from flask import render_template, request, redirect
from flask_login import login_required, login_user, logout_user
from app import app
from models import *
from forms import CommentsForm, RegisterForm, LoginForm




# Index page
@app.route('/', methods=['GET'])
def index():
    books = Book.query.all()

    return render_template('index.html', active='index', books=books)



# Product page
@app.route('/product', methods=['GET', 'POST'])
def product():

    book = Book.query.filter(Book.discount_price != Book.price).first()
    book_id = book.id
    
    language = Language.query.filter(Language.id.in_(db.select([Language_Book.language_id]).filter(Language_Book.book_id == book_id))).all()
    genre = Genre.query.filter(Genre.id.in_(db.select([Genre_Book.genre_id]).filter(Genre_Book.book_id == book_id))).all()
    comments = Comments().query.filter(Comments.book_id==book_id).all()

    posted_data = request.form

    form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(data = posted_data)
        if form.validate_on_submit():
            comment = Comments(full_name=posted_data['full_name'], message=posted_data['message'], created_at=datetime.now().strftime('%d %B %Y'), book_id = book_id)
            Comments.add(comment)

    return render_template('product.html', book=book, active='product', genre=genre, language=language, form=form, comments=comments)



# Book detail page
@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = Book.query.all()[book_id-1]
    language = Language.query.filter(Language.id.in_(db.select([Language_Book.language_id]).filter(Language_Book.book_id == book_id))).all()
    genre = Genre.query.filter(Genre.id.in_(db.select([Genre_Book.genre_id]).filter(Genre_Book.book_id == book_id))).all()
    comments = Comments().query.filter(Comments.book_id==book_id).all()

    posted_data = request.form

    form = CommentsForm()

    print((comments))

    if request.method == 'POST':   
        form = CommentsForm(data = posted_data)
        if form.validate_on_submit():
            comment = Comments(full_name=posted_data['full_name'], message=posted_data['message'], created_at=datetime.now().strftime('%d %B %Y'), book_id = book_id)
            Comments.add(comment)

    return render_template('book.html', book=book, language=language, genre=genre, form=form, comments=comments)


# Users
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        posted_data = request.form

        form = RegisterForm(data = posted_data)
        if form.validate_on_submit():
            new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, username=form.username.data, password=form.password.data)
            new_user.save()
    return render_template('register.html', form = form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        posted_data = request.form
        form = LoginForm(data = posted_data)

        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first() 
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('/')
    return render_template('login.html', form = form)
