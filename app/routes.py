from flask import render_template, flash, redirect
from app import app, db
from app.forms import NewArtistForm, LoginForm, RegistrationForm, NewEventForm, NewVenueForm
from app.models import Artist, User, Venue, Event, eventtoartist_identifier
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from werkzeug.urls import url_parse
import random


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/artistlist')
@login_required
def view():
    artists = Artist.query.all()
    return render_template('artistlist.html', title='Artist List', artists=artists)


@app.route('/artist/<name>')
@login_required
def artist(name):
    artist1 = Artist.query.filter_by(name=name).first()
    return render_template('artist.html', title="artist", artistinfo=artist1)


@app.route('/CreateAnArtist', methods=['GET', 'POST'])
@login_required
def create():
    form = NewArtistForm()
    if form.validate_on_submit():
        artist = Artist(name=form.name.data, hometown=form.hometown.data, description=form.description.data)
        db.session.add(artist)
        db.session.commit()
        flash('The new Artist, {}, has been created!'.format(
            form.name.data))
        return render_template('artist.html', title=form.name.data, artistinfo=artist)
    return render_template('CreateAnArtist.html', title='Create An Artist', form=form)

@app.route('/CreateAVenue', methods=['GET', 'POST'])
@login_required
def createVenue():
    form = NewVenueForm()
    if request.method == 'POST':
        venue = Venue(name=form.name.data, street=form.street.data, city=form.city.data, state=form.state.data, zip=form.zip.data)
        db.session.add(venue)
        db.session.commit()
        flash('The new Venue, {}, has been created!'.format(
            form.name.data))
        return render_template('artistlist.html')
    return render_template('CreateAVenue.html', title='Create An Artist', form=form)

@app.route('/CreateAnEvent', methods=['GET', 'POST'])
@login_required
def createEvent():
    # venuesQ = Venue.query.all()
    # venueArray = []
    # for venue in venuesQ:
    #     venueArray.append((venue.venue_id, venue.name))
    form = NewEventForm()
    form.set_choices()
    # venuesQ = Venue.query.all()
    # venueArray = []
    # for venue in venuesQ:
    #     venueArray.append(venue.name)
    selectedArtistIDList = form.artistField.data
    #request.method == 'POST'
    #
    # Event.query.get(id)
    if form.validate_on_submit():
        # form.validate_name(form.name.data)
        newEvent = Event(name=form.name.data, date=form.date.data, event_venue_id=int(form.venueField.data))
        db.session.add(newEvent)
        artistList = []
        for id in selectedArtistIDList:
            artistList.append(Artist.query.get(id))
        for artist in artistList:
            artist.events.append(newEvent)
        db.session.commit()
        return redirect(url_for('index'))
    # flash('error: {}'.format(form.errors))
    return render_template('CreateAnEvent.html', title='Create An Event', form=form)


@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")
   # clear all data from all tables
   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())

   db.session.commit()
   artist1 = Artist(name="Bob", hometown="Ithaca", description="I like to rock out")
   artist2 = Artist(name="John", hometown="Jacksonville", description="I like to rock out")
   artist3 = Artist(name="The Ithacans", hometown="Saratoga Springs", description="I like to rock out")
   artist4 = Artist(name="South Hill Band", hometown="Ithaca", description="I like to rock out")
   venue1 = Venue(name='The First Venue', street="Music Street", city="Mount Soyer", state="New York", zip=987649)
   venue2 = Venue(name='The Second Venue', street="South Street", city="Boston", state="New Jersey", zip=728492)
   venue3 = Venue(name='The Third Venue', street="Main Street", city="New York City", state="Maine", zip=849308)

   return render_template('index.html')