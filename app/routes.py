from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/artistlist')
def view():
    artists = [
            {
                'name': 'Jill Ackerman',
                'shortname': 'JillAckerman',
            },
            {
                'name': 'Holly Adams',
                'shortname': 'HollyAdams',
            },
            {
                'name': 'Ben Altman',
                'shortname': 'BenAltman',
            }
    ]
    return render_template('artistlist.html', title='Artist List', artists=artists)


@app.route('/JillAckerman')
def jill():
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
    return render_template('JillAckerman.html', title='Jill Ackerman', artistinfo=artistinfo)


@app.route('/HollyAdams')
def Holly():

    return render_template('HollyAdams.html', title='Holly Adams')


@app.route('/BenAltman')
def Ben():

    return render_template('BenAltman.html', title='Ben Altman')


@app.route('/CreateAnArtist')
def Create():

    return render_template('CreateAnArtist.html', title='Create An Artist')