from flask import request
from flask_praetorian import auth_required, current_user
from app import app

@app.route('/api/profile')
@auth_required
def profile():
    return {'message': f'Profile of user \'{current_user().email}\''}
