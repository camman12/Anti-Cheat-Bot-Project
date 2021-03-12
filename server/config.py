import os

DEBUG = True

SECRET_KEY = 'secret'  # CHANGE THIS

JWT_ACCESS_LIFESPAN = {'hours': 24}
JWT_REFRESH_LIFESPAN = {'days': 30}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(os.getcwd(), "database.sqlite")}'

# APScheduler config
SCHEDULER_API_ENABLED = True
JOBS = [
    {
        'id': 'No1',  # 任务唯一ID
        'func': 'app.test:shishi',  # name `shishi`
        'args': '',  # 如果function需要参数，就在这里添加
        'trigger': {
            'type': 'cron',  # 类型
            # 'day_of_week': "0-6", # 可定义具体哪几天要执行
            # 'hour': '*', # 小时数
            # 'minute': '1',
            'second': '*/10'  # "*/3" 表示每3秒执行一次，单独一个"3" 表示每分钟的3秒。现在就是每一分钟的第3秒时循环执行。
        }
    }
]
