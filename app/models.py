from . import db

from datetime import datetime


class Stock(db.Model):
    __tablename__ = 'Stock'
    StockId = db.Column(db.String(20), primary_key=True)
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
    CreateTime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )
    UpdateTime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )

    def to_json(self):
        return {
            'StockId': self.StockId,
            'StockName': self.StockName,
            'PriceNow': self.PriceNow,
            'VolumeNow': self.VolumeNow,
            'VolumeAll': self.VolumeAll,
            'OpenPrice': self.OpenPrice,
            'HighestPrice': self.HighestPrice,
            'LowestPrice': self.LowestPrice,
            'ClosingPrice': self.ClosingPrice,
            'Increase': self.Increase,
            'Amplitude': self.Amplitude,
            'Updown': self.Updown,
            'FavoriteCount': self.FavoriteCount,
            'CreateTime': self.CreateTime,
            'UpdateTime': self.UpdateTime,
        }

    def __repr__(self):
        return f'<Stock {self.StockName!r}>'
