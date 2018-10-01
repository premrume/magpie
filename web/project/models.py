from project import db
from datetime import datetime

class Paper(db.Model):

    __tablename__ = "papers"

    id = db.Column(db.String(36), unique=True, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    orig_filename = db.Column(db.String, default=None, nullable=True)
    uuid_filename = db.Column(db.String, default=None, nullable=True)
    posted_url = db.Column(db.String, default=None, nullable=True)
    posted_timestamp = db.Column(db.DateTime, nullable=True)
    component = db.Column(db.String(36))
    status = db.Column(db.String(36))
    msg = db.Column(db.String(36))

    def __init__(self, id, title, f1, u1, f2 ):
        self.status = 'UPLOAD'
        self.component = 'magpie'
        self.msg = 'Work in progress'
        self.id = id
        self.title = title
        self.orig_filename = f1
        self.uuid_filename = f2
        self.posted_url = u1
        self.posted_timestamp = datetime.now()

    def __repr__(self):
        return '<title {}'.format(self.title)
