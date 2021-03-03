DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'outcome'
PASSWORD = 'ALHc79JvoHmxJ9Xifj'
HOST = 'rm-wz9yxho9eg3x33hpono.mysql.rds.aliyuncs.com'
PORT = '3306'
DATABASE = 'anticheat'

#mysql 不会认识utf-8,而需要直接写成utf8
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True