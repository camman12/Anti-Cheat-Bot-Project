from flask import request
from app import app, db, guard, User


@app.route('/api/register', methods=['POST'])
def register():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.
    .. example::
       $ curl http://localhost:5000/api/register -X POST \
         -d '{"email":"user@example.com","password":"strongpassword"}'
    """
    req = request.get_json(force=True)
    email = req.get('email', None)
    password = req.get('password', None)

    user = User(
        email=email,
        password=guard.hash_password(password),
        roles='admin'
    )

    db.session.add(user)
    db.session.commit()

    ret = {'access_token': guard.encode_jwt_token(user)}
    return ret, 200
