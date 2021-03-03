from flask import Flask


# 引用 APSchedule
from flask_apscheduler import APScheduler
# 引用 congfig 配置
from config import APSchedulerJobConfig

app = Flask(__name__, static_folder='../../client/build')


 
# 定时任务，导入配置
# APSchedulerJobConfig 就是在 config.py文件中的 类 名称。
app.config.from_object(APSchedulerJobConfig)
 
# 初始化Flask-APScheduler，定时任务
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


from app.views import index, keyword