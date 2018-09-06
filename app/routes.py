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
                'bio': 'I am a ceramic artist and teacher. My functional designs are wheel thrown or hand-built and fired to a gas or wood fired appearance.',
                'hometown': 'Ithaca New York'
            },
            {
                'name': 'Holly Adams',
                'bio': 'A SAG-AFTRA Performer, my work includes Stage, Film, and Voice Over. I also have expertise as a Teaching Artist, Mask-maker, and in stage combat.',
                'hometown': 'Ithaca New York'
            },
            {
                'name': 'Ben Altman',
                'bio': 'I am a visual artist using photography, video, performance and installation. I am fascinated by violent modern history and how it forms our contemporary world.',
                'hometown': 'Ithaca New York'
            }
    ]
    return render_template('artistlist.html', title='Artist List', artists=artists)

