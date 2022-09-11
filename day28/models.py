from extensions import db
from app import app as app


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float)
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