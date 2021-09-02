import json
from datetime import datetime

import requests
from flask import jsonify, request

from .. import db
from ..models import Stock
from . import api


def stock_crawler(stock_ids):
    stock_urls = '|'.join(f'tse_{stock_id}.tw' for stock_id in stock_ids)

    url = f'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_urls}'
    response = requests.get(url)
    print(response)
    stocks = response.json()['msgArray']

    # with open('./stock.json') as file:
    #     stocks = json.loads(file.read())['msgArray']

    json_to_db_keys = {
        'c': 'StockId',  # 股票代號
        'n': 'StockName',  # 公司簡稱
        'z': 'PriceNow',  # 當盤成交價
        'tv': 'VolumeNow',  # 當盤成交量
        'v': 'VolumeAll',  # 累積成交量
        'o': 'OpenPrice',  # 開盤價
        'h': 'HighestPrice',  # 最高價
        'l': 'LowestPrice',  # 最低價
        'y': 'ClosingPrice',  # 昨收價
    }

    for stock in stocks:
        old_stock = Stock.query.get(stock['c'])
        new_stock = old_stock if old_stock else Stock()

        for json_key, db_key in json_to_db_keys.items():
            value = stock[json_key] if json_key in ['c', 'n'] else float(
                stock[json_key])
            setattr(new_stock, db_key, value)

        # 漲幅 = (當盤成交價 - 昨收價) / 昨收價 * 100
        new_stock.Increase = (new_stock.PriceNow - new_stock.ClosingPrice
                              ) / new_stock.ClosingPrice * 100

        # 振幅 = (最高價 - 最低價) / 昨收價 * 100
        new_stock.Amplitude = (new_stock.HighestPrice - new_stock.LowestPrice
                               ) / new_stock.ClosingPrice * 100

        # 漲跌區間 = 當盤成交價 - 開盤價
        new_stock.Updown = new_stock.PriceNow - new_stock.OpenPrice

        new_stock.UpdateTime = datetime.utcnow()

        db.session.add(new_stock)
        db.session.commit()

    return Stock.query.filter(Stock.StockId.in_(stock_ids)).all()


@api.route('/stock')
def get_stocks():
    stock_ids = request.args.getlist('stock_id', type=str)
    stocks = stock_crawler(stock_ids)
    return jsonify([stock.to_json() for stock in stocks])
