from app import db

class EventToArtist(db.Model):
    __tablename__ = 'EventToArtist'
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'), primary_key=True)
    # event = db.relationship("Event", back_populates="events")
    # artist = db.relationship("Artist", back_populates="artists")

class Artist(db.Model):
    __tablename__ = 'Artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    hometown = db.Column(db.String(128))
    description = db.Column(db.String(256))
    # artists = db.relationship("EventToArtist", back_populates="event")


    def __repr__(self):
        return "<Artist {}".format(self.firstname)

class Event(db.Model):
    __tablename__ = 'Event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    date = db.Column(db.String(64))
    # events = db.relationship("EventToArtist", back_populates="artist")


    def __repr__(self):
        return "<Event {}".format(self.name)