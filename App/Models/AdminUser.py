# AdminUser.py 数据库模型
from App.exts import db  # 导入sqlalchemy插件


class AdminUser(db.Model):
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    username = db.Column(db.String(20), nullable=False)  # 用户名
    password = db.Column(db.String(20), nullable=False)  # 密码--明文
    email = db.Column(db.String(20), nullable=False)  # 邮箱
    phone = db.Column(db.String(20), nullable=False)  # 手机号


    def __init__(self, username, password, email='', phone=''):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone


