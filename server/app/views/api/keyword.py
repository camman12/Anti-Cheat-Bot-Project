from flask import request
from app import app, db, Data
import json
from .google import Crawler as GoogleCrawler


@app.route('/api/keyword', methods=['POST'])
def add_keyword():
    print(request.get_json())
    data = request.get_json()
    print(data['keyword'])
    keyword = data['keyword']
    gc = GoogleCrawler('1', [keyword], 1)
    url = gc.base_url + 'search?q=' + keyword
    gc.search(url, keyword, 1)
    datas = gc.data_list
    return {
        'data': datas,
        'success': True
    }
