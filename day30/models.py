from email.policy import default
from sqlalchemy import ForeignKey
from extensions import db, login_manager
from app import app as app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float)
    discount_price = db.Column(db.Float, default=price)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    stock = db.Column(db.Integer)
    publisher = db.Column(db.String(100))


    def __repr__(self):
        return self.title

    def add(self):
        db.session.add(self)
        db.session.commit()


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))

    def __repr__(self):
        return self.name

    def add(self):
        db.session.add(self)
        db.session.commit()


class Language(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    language = db.Column(db.String(200))

    def __repr__(self):
        return self.language

    def add(self):
        db.session.add(self)
        db.session.commit()


class Language_Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        return self.language_id

    def add(self):
        db.session.add(self)
        db.session.commit()


class Genre_Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        return self.genre_id

    def add(self):
        db.session.add(self)
        db.session.commit()

    
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.String(20), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))


    def __repr__(self):
        return self.full_name


    def add(self):
        db.session.add(self)
        db.session.commit()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        return self.username

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, first_name, last_name, password, email, username, is_active = True, is_superuser = False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)
        self.username = username
        self.is_active = is_active
        self.is_superuser = is_superuser

    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, password):
        return check_password_hash(self.password, password) 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)