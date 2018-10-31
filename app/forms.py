from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from app.models import Artist, User, Venue, Event
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional, AnyOf

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


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class NewVenueForm(FlaskForm):
    name = StringField('Enter the venue name', validators=[DataRequired()])
    street = StringField('Enter the venue street', validators=[DataRequired()])
    city = StringField('Enter the venue city', validators=[DataRequired()])
    state = StringField('Enter the venue state', validators=[DataRequired()])
    zip = StringField('Enter the venue zipcode', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        user = Venue.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please enter a different venue.')


class NewEventForm(FlaskForm):
    name = StringField('Enter the event name', validators=[DataRequired()])
    date = StringField('Enter the event date', validators=[DataRequired()])
    venueField = SelectField('Please select a venue for the event', validators=[DataRequired()], coerce=int)
    artistField = SelectMultipleField('Please select an artist(s)', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Submit')

    def set_choices(self):
        venuesQ = Venue.query.all()
        venueArray = []
        for venue in venuesQ:
            venueArray.append((venue.venue_id, venue.name))
        self.venueField.choices = venueArray
        artistsQ = Artist.query.all()
        artistArray = []
        for artist in artistsQ:
            artistArray.append((artist.artist_id, artist.name))
        self.artistField.choices = artistArray


    def validate_name(self, name):
        event = Event.query.filter_by(name=name.data).first()
        if event is not None:
            raise ValidationError('Please enter a different name.')

    def validate_venueField(self, venueField):
        if venueField.data is None:
            raise ValidationError('Please enter a venue.')

    def validate_artistField(self, artistField):
        if artistField.data is None:
            raise ValidationError('Please enter a artist.')
