from flask import Flask

app = Flask(__name__, static_folder='../../client/build')

from app.views import index, keyword