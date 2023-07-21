from App.exts import db  # 导入sqlalchemy插件


class SoccerTeam(db.Model):
    __tablename__ = 'soccer_team'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    teamName = db.Column(db.String(20), nullable=False)  # 球队名
    content = db.Column(db.String(20), nullable=False)  # 球队简介
    soccerPlayers = db.relationship('SoccerPlayer', backref='team', lazy=True)  # 球员外键
    is_delete = db.Column(db.Boolean, default=False)  # 是否删除
