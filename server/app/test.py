from app import app, db, Task
from crawler.google import Crawler


def shishi():
    with app.app_context():
        datas = Task.query.filter_by(status=0)

        for data in datas:
            data.update(status=1)
            # print(data)
            print(data['task_id'])
            print(data['keywords'])
            print(data['delay_sec'])
            task_id = data['task_id']
            keywords = data['keywords'].split(',')
            delay_sec = data['delay_sec']
            c = Crawler(task_id, keywords, delay_sec)
            c.main()

        db.session.commit()
