from flask import request
from app import app, guard

@app.route('/api/login', methods=['POST'])
def login():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.
    .. example::
       $ curl http://localhost:5000/api/login -X POST \
         -d '{"email":"user@example.com","password":"strongpassword"}'
    """
    req = request.get_json(force=True)
    email = req.get('email', None)
    password = req.get('password', None)
    user = guard.authenticate(email, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    return ret, 200
