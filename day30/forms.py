from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class CommentsForm(FlaskForm):
    full_name = StringField(label="Tam adınız:", validators=[DataRequired(), Length(min=3, max=20)])
    message = TextAreaField(label="Şərhiniz:", validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField(label="Username:", validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField(label="Password:", validators=[DataRequired(), Length(min=3, max=30)])

class RegisterForm(FlaskForm):
    first_name = StringField(label="First name:", validators=[DataRequired(), Length(min=3, max=30)])
    last_name = StringField(label="Last name:", validators=[DataRequired(), Length(min=3, max=30)])
    email = EmailField(label="Email:", validators=[DataRequired(), Email(), Length(min=3, max=30)])
    username = StringField(label="Username:", validators=[DataRequired(), Length(min=3, max=30)])
    password = StringField(label="Password:", validators=[DataRequired(), Length(min=3, max=40)])