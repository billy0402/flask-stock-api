from datetime import datetime

from flask import jsonify, request
from GoogleNews import GoogleNews

from . import api


@api.route('/news')
def get_news():
    keyword = request.args.get('keyword', '', type=str)
    date = datetime.today()

    googlenews = GoogleNews()
    googlenews.set_encode('utf-8')
    googlenews.set_lang('zh-tw')
    googlenews.set_time_range('01/01/2021', date.strftime('%m/%d/%Y'))
    googlenews.search(keyword)
    links = googlenews.get_links()
    titles = googlenews.gettext()

    result = [{
        'link': link,
        'title': title,
    } for link, title in zip(links, titles)]

    return jsonify(result[:3])
