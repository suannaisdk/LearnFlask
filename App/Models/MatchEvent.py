from App.exts import db  # 导入sqlalchemy插件


class MatchEvent(db.Model):
    __tablename__ = 'match_event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    match_id = db.Column(db.Integer, db.ForeignKey('soccer_match.id'))   # 比赛的id
    event_time = db.Column(db.DateTime)  # 事件时间
    event_team_id = db.Column(db.Integer, db.ForeignKey('soccer_team.id')) # 队伍id
    event_goal_player_id = db.Column(db.Integer, db.ForeignKey('soccer_player.id')) # 队伍id
    event_assist_player_id = db.Column(db.Integer, db.ForeignKey('soccer_player.id')) # 队伍id

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
