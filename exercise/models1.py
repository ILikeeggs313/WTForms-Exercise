from flask_sqlalchemy import SQLAlchemy


def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"
db = SQLAlchemy()

#models go below!
class Pet(db.Model):
    """Single pet model showing a potentially adoptable pet 
    including: id, name, species, photo_url, age, notes, availablability """
    __tablename__ = "pets"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def image_url(self):
        """Image for pet if inserted"""
        return self.photo_url or DEFAULT_IMAGE
