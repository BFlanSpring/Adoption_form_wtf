from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pets(db.Model):
    """Pets"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.Text,
                    nullable=False)
    species = db.Column(db.Text,
                        nullable=False) 
    image_link = db.Column(db.Text,
                        nullable=True) 
    age = db.Column(db.Integer,  
                    nullable=True)  
    notes = db.Column(db.Text, 
                    nullable=True)  
    available = db.Column(db.Boolean,
                        nullable=False,
                        default=True)  


def connect_db(app):
    db.app = app
    with app.app_context():
        db.create_all()
