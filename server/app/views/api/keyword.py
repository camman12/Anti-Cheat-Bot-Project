from flask import request
from app import app

@app.route('/api/keyword', methods=['POST'])
def add_keyword():
    print(request.get_json())
    return {'success': True}