# models.py 数据库模型
from .exts import db  # 导入sqlalchemy插件


class SoccerPlayer(db.Model):
    __tablename__ = 'soccer_player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    name = db.Column(db.String(20), nullable=False)  # 姓名
    # birthday = db.Column(db.DateTime, nullable=False)  # 生日
    avatarImg = db.Column(db.Text(), nullable=False)  # 头像
    height = db.Column(db.Float, nullable=False)  # 身高
    weight = db.Column(db.Float, nullable=False)  # 体重
    goals = db.Column(db.Integer, nullable=False)  # 进球数
    assist = db.Column(db.Integer, nullable=False)  # 助攻数
    soccerTeam_id = db.Column(db.Integer, db.ForeignKey('soccer_team.id'))  # 球队外键，外键写在多的一方
    is_delete = db.Column(db.Boolean, default=False)  # 是否删除


class SoccerTeam(db.Model):
    __tablename__ = 'soccer_team'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    teamName = db.Column(db.String(20), nullable=False)  # 球队名
    content = db.Column(db.String(20), nullable=False)  # 球队简介
    soccerPlayers = db.relationship('SoccerPlayer', backref='team', lazy=True)  # 球员外键
    is_delete = db.Column(db.Boolean, default=False)  # 是否删除


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


