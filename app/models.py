from app import db

class Bucketlist(db.Model):
    """
    This class repressent the bucketlist table.
    """

    __tablename__ = 'bucketlists'

    id = db.Column(db.Inteder, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name):
        """
        initialize with name
        """
        self.name = name

    def save(self):
        db.session.add(self)
        de.session.commit()

    @staticmethod
    def get_all():
        return Bucketlist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "f<Bucketlist: {self.name}"
