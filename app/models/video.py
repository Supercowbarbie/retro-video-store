from flask import current_app
from app import db

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    total_copies = db.Column(db.Integer)
    availible_inventory = db.Column(db.Integer)

    def make_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "total_inventory": self.total_copies,
            # "availible_inventory": self.availible_inventory
                    }
    