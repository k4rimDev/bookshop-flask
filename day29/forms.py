from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class CommentsForm(FlaskForm):
    full_name = StringField(label="Tam adınız:", validators=[DataRequired(), Length(min=3, max=40)])
    message = TextAreaField(label="Şərhiniz:", validators=[DataRequired()])