# exts.py 插件管理
from flask_restful import Api

# 初始化插件
api = Api()


# 初始化插件
def init_ext(app):
    api.init_app(app=app)   # 初始化api插件
