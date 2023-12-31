from App.exts import db  # 导入sqlalchemy插件


# 足球比赛表
class SoccerMatch(db.Model):
    __tablename__ = 'soccer_match'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    home_team_id = db.Column(db.Integer, db.ForeignKey('soccer_team.id'))  # 主队外键
    guest_team_id = db.Column(db.Integer, db.ForeignKey('soccer_team.id'))  # 客队外键
    match_time = db.Column(db.DateTime)  # 比赛时间
    match_address = db.Column(db.String(20))  # 比赛地点
    match_content = db.Column(db.String(20))  # 比赛简介
    match_status = db.Column(db.Integer, default=0)  # 比赛状态，0未开始，1比赛开始，2比赛结束
    match_events = db.relationship('MatchEvent', backref='event', lazy=True)  # 事件外键
    home_goals = db.Column(db.Integer, default=0)  # 主队进球数
    guest_goals = db.Column(db.Integer, default=0)  # 客队进球数
    is_delete = db.Column(db.Boolean, default=False)  # 是否删除

    def __init__(self, home_team_id, guest_team_id, **kwargs):
        self.home_team_id = home_team_id
        self.guest_team_id = guest_team_id
        for key, value in kwargs.items():
            setattr(self, key, value)
