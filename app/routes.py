from flask import render_template, flash, redirect
from app import app, db
from app.forms import NewArtistForm
from app.models import Artist, Event
from flask import render_template, flash, redirect, url_for, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/artistlist')
def view():
    artists = Artist.query.all()
    return render_template('artistlist.html', title='Artist List', artists=artists)


@app.route('/artist/<name>')
def artist(name):
    artist1 = Artist.query.filter_by(name=name).first()
    events = artist1.events
    if artist1 is None:
        flash("The artist {} was not found".format(artist1.name))
        return render_template('artistlist.html')
    else:
        listofevents = []
        for event in events:
            listofevents.append(event)

    return render_template('artist.html', title="artist", artistinfo=artist1)


@app.route('/CreateAnArtist', methods=['GET', 'POST'])
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


@app.route('/reset_db')
def reset_db():
   flash("Resetting database: deleting old data and repopulating with dummy data")
   # clear all data from all tables
   meta = db.metadata
   for table in reversed(meta.sorted_tables):
       print('Clear table {}'.format(table))
       db.session.execute(table.delete())
   db.session.commit()