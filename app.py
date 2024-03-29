from app import app, db
from app.models import Artist, Event


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Event': Event, 'Artist': Artist}