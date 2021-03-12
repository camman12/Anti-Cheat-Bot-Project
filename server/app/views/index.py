import os
from flask import send_from_directory
from app import app


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    # Send static files if they exist, else send index.html
    if path != '' and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
