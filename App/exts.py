# exts.py 插件管理
from flask_restful import Api   # 导入restful插件
from flask_sqlalchemy import SQLAlchemy   # 导入sqlalchemy插件
from flask_migrate import Migrate   # 导入数据库迁移插件

# 初始化插件
api = Api()
db = SQLAlchemy()
migrate = Migrate()


# 初始化插件
def init_ext(app):
    api.init_app(app=app)   # 初始化api插件
    db.init_app(app=app)    # 初始化sqlalchemy插件
    migrate.init_app(app=app, db=db)    # 初始化数据库迁移插件
