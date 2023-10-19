from flask import Flask
from .exts import init_ext
from .urls import *     # 导入路由规则
from datetime import timedelta

# 初始化App，创建App都在此进行设置
def create_app():
    app = Flask(__name__)  # 创建app

    # 配置数据库
    db_uri = 'sqlite:///soccerSqlite3.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象追踪修改。默认false
    app.config['JWT_SECRET_KEY'] = 'secret'  # 设置jwt加密密钥
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=15)
    # 初始化插件
    init_ext(app)

    return app
