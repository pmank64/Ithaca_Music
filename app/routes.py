from flask import render_template, flash, redirect
from app import app
from app.forms import NewArtistForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/artistlist')
def view():
    artists = [
            {
                'name': 'Jill Ackerman'

            },
            {
                'name': 'Holly Adams'
            },
            {
                'name': 'Ben Altman'
            }
    ]
    return render_template('artistlist.html', title='Artist List', artists=artists)


@app.route('/artist')
def viewArtist():
    artistinfo = [
        {
            'name': 'Jill Ackerman',
            'bio': 'I am a ceramic artist and teacher. My functional designs are wheel thrown or hand-built and fired to a gas or wood fired appearance.',
            'hometown': 'Ithaca New York',
            'imgURL': 'https://i.etsystatic.com/isla/cae73e/21674604/isla_500x500.21674604_9wmhf101.jpg?version=0',
            'event': 'Ithaca Artist Market',
            'eventDesc': 'The Ithaca Artist Market fills all 88 booths at the Ithaca Farmers Market with regional fine and functional artists in a unique, once-a-year, cant miss event. Over 80 established visual artists have been juried into the Market to showcase and sell a stunning variety of some of the best fine art in the region.'
        }
    ]
    return render_template('artist.html', title="artist", artistinfo=artistinfo)


@app.route('/CreateAnArtist', methods=['GET', 'POST'])
def create():
    form = NewArtistForm()
    if form.validate_on_submit():
        flash('The new Artist, {}, has been created!'.format(
            form.name.data))
        newArtist = [
            {
                'name': form.name.data,
                'bio': form.description.data,
                'hometown': form.hometown.data,
                'event': 'none'
            }
        ]
        return render_template('artist.html', title=form.name.data, artistinfo=newArtist)
    return render_template('CreateAnArtist.html', title='Create An Artist', form=form)