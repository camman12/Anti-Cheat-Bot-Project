from flask import request
from flask_praetorian import auth_required, current_user
from app import app, db, Data
from app.models import Keyword
import json
from .google import Crawler as GoogleCrawler


@app.route('/api/keyword', methods=['POST'])
@auth_required
def add_keyword():
    user = current_user()
    data = request.get_json()
    keyword = data['keyword']

    keyword_row = Keyword.lookup(keyword)

    if not keyword_row:
        keyword_row = Keyword()
        keyword_row.text = keyword

    user.keywords.append(keyword_row)

    db.session.add(keyword_row)
    db.session.commit()

    return {
        'success': True
    }


@app.route('/api/keywords', methods=['GET'])
@auth_required
def get_keywords():
    user = current_user()

    keyword_strs = []

    for keyword in user.keywords:
        keyword_strs.append(keyword.text)

    return {
        'keywords': keyword_strs
    }


@app.route('/api/keyword/delete', methods=['DELETE'])
@auth_required
def delete_keyword():
    user = current_user()
    data = request.get_json()

    match = Keyword.lookup(data['keyword'])

    if match:
        user.keywords.remove(match)
        db.session.commit()
        return {
            'success': True
        }

    return {
        'success': False
    }, 400
