from . import db

from datetime import datetime


class Stock(db.Model):
    __tablename__ = 'Stock'
    StockId = db.Column(db.Integer, primary_key=True)
    StockName = db.Column(db.String(50), unique=True, nullable=False)
    PriceNow = db.Column(db.Float, nullable=False)
    VolumeNow = db.Column(db.Float, nullable=False)
    VolumeAll = db.Column(db.Float, nullable=False)
    OpenPrice = db.Column(db.Float, nullable=False)
    HighestPrice = db.Column(db.Float, nullable=False)
    LowestPrice = db.Column(db.Float, nullable=False)
    ClosingPrice = db.Column(db.Float, nullable=False)
    Increase = db.Column(db.Float, nullable=False)
    Amplitude = db.Column(db.Float, nullable=False)
    Updown = db.Column(db.Float, nullable=False)
    FavoriteCount = db.Column(db.Integer, nullable=False, default=0)
    CreateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    UpdateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f'<Role {self.name!r}>'
