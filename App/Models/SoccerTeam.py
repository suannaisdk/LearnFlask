from App.exts import db  # 导入sqlalchemy插件


class SoccerTeam(db.Model):
    __tablename__ = 'soccer_team'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    team_name = db.Column(db.String(20), nullable=False)  # 球队名
    logo_img_url = db.Column(db.Text(), nullable=True)  # 球队logo
    content = db.Column(db.String(20), nullable=True)  # 球队简介
    home_matches = db.relationship('SoccerMatch', backref='home_team', lazy=True, foreign_keys='SoccerMatch.home_team_id')  # 比赛外键
    guest_matches = db.relationship('SoccerMatch', backref='guest_team', lazy=True, foreign_keys='SoccerMatch.guest_team_id')  # 比赛外键
    soccer_players = db.relationship('SoccerPlayer', backref='team', lazy=True)  # 球员外键
    is_delete = db.Column(db.Boolean, default=False)  # 是否删除

    def __init__(self, team_name, content=''):
        self.team_name = team_name
        self.content = content
