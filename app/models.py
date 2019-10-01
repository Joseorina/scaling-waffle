from app import db

class Bucketlust(db.Model):
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
        pass

    @staticmethod
    def get_all():
        pass

    def delete(self):
        pass

    def __repr__(self):
        pass
