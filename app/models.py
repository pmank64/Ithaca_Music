from app import db, login
from datetime import datetime
from hashlib import md5
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

eventtoartist_identifier = db.Table('eventtoartist_identifier',
    db.Column('artist_id', db.Integer, db.ForeignKey('artists.artist_id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('events.event_id'), primary_key=True)
)

class Artist(db.Model):
    __tablename__ = 'artists'
    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    hometown = db.Column(db.String(128))
    description = db.Column(db.String(256))
    events = db.relationship("Event", secondary=eventtoartist_identifier)

    def __repr__(self):
        return "<Artist {}".format(self.name)

class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    date = db.Column(db.String(64))
    event_venue_id = db.Column(db.Integer, db.ForeignKey('venues.venue_id'))

    def __repr__(self):
        return "<Event {}".format(self.name)


class Venue(db.Model):
    __tablename__ = 'venues'
    venue_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    street = db.Column(db.String(128))
    city = db.Column(db.String(128))
    state = db.Column(db.String(64))
    zip = db.Column(db.Integer)
    events = db.relationship('Event', backref="venue", lazy='dynamic')

    def __repr__(self):
        return "<Venue {}".format(self.name)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))