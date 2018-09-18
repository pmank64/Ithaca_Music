from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class NewArtistForm(FlaskForm):
    # fields of the form are represented by class variables
    name = StringField('Enter the artist name', validators=[DataRequired()])
    hometown = StringField('Enter the artist hometown', validators=[DataRequired()])
    description = TextAreaField('Enter the artist description', validators=[DataRequired()])
    submit = SubmitField('Submit')
