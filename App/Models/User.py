# 用户登录模型
from App.exts import db  # 导入sqlalchemy插件


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    username = db.Column(db.String(20), nullable=False)  # 用户名
    password = db.Column(db.String(20), nullable=False)  # 密码--明文
    is_admin = db.Column(db.Boolean, default=False)  # 是否是管理员
    soccer_player_id = db.Column(db.Integer, db.ForeignKey("soccer_player.id"))  # 球员外键

    def __init__(self, username, password, is_admin=False, soccer_player_id=None):
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.soccer_player_id = soccer_player_id
