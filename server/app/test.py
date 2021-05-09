from app import app, db, Task
from crawler.google import Crawler


def shishi():
    with app.app_context():
        datas = Task.query.filter_by(status=0)
        print(datas)

        for data in datas:
            data.status = 1
            # print(data)
            print(data.id)
            print(data.keywords)
            print(data.delay_sec)
            task_id = data.id
            keywords = data.keywords.split(',')
            delay_sec = data.delay_sec
            c = Crawler(task_id, keywords, delay_sec)
            c.main()

        db.session.commit()
