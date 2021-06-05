from app import app, db, Task
from app.models import User
from crawler.google import Crawler


def shishi():
    with app.app_context():
        users = User.query.all()

        for user in users:
            if len(user.keywords) == 0:
                continue

            keywords = [keyword.text for keyword in user.keywords]

            c = Crawler(0, keywords, 1)
            c.main()
