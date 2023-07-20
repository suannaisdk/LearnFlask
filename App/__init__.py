from flask import Flask
from .exts import init_ext
from .urls import *     # 导入路由规则


# 初始化App，创建App都在此进行设置
def create_app():
    app = Flask(__name__)  # 创建app
    # 初始化插件
    init_ext(app)

    return app
