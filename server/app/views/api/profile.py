from flask_praetorian import auth_required, current_user
from app import app


@app.route('/api/profile')
@auth_required
def profile():
    user = current_user()
    print(user)

    return {
        'email': user.email,
        'roles': user.roles,
        'is_active': user.is_active,
    }
