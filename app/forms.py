from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from app.models import Artist
from wtforms.validators import ValidationError, DataRequired

class NewArtistForm(FlaskForm):
    # fields of the form are represented by class variables
    name = StringField('Enter the artist first name', validators=[DataRequired()])
    hometown = StringField('Enter the artist hometown', validators=[DataRequired()])
    description = TextAreaField('Enter the artist description', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        user = Artist.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please enter a different name.')
