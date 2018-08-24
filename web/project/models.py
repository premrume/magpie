from project import db
from datetime import datetime

class Paper(db.Model):

    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    jpg_filename = db.Column(db.String, default=None, nullable=True)
    jpg_url = db.Column(db.String, default=None, nullable=True)
    jpg_timestamp = db.Column(db.DateTime, nullable=True)

    def __init__(self, title, f1, u1 ):
        self.title = title
        self.jpg_filename = f1
        self.jpg_url = u1
        self.jpg_timestamp = datetime.now()

    def __repr__(self):
        return '<title {}'.format(self.title)
