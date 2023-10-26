from App.exts import db  # 导入sqlalchemy插件


class SoccerPlayer(db.Model):
    __tablename__ = 'soccer_player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    name = db.Column(db.String(20), nullable=False)  # 姓名
    birthday = db.Column(db.String(20), nullable=True)  # 生日
    avatar_img = db.Column(db.Text(), nullable=True)  # 头像
    number = db.Column(db.Integer, nullable=True)  # 号码
    height = db.Column(db.Float, nullable=True)  # 体重
    weight = db.Column(db.Float, nullable=True)  # 体重
    attendance = db.Column(db.Integer, nullable=True)  # 出场次数
    goals = db.Column(db.Integer, nullable=True)  # 进球数
    assist = db.Column(db.Integer, nullable=True)  # 助攻数
    soccer_team_id = db.Column(db.Integer, db.ForeignKey('soccer_team.id'))  # 球队外键，外键写在多的一方
    goals_events = db.relationship('MatchEvent', backref="goal_player", lazy=True, foreign_keys='MatchEvent.event_goal_player_id')
    assist_events = db.relationship('MatchEvent', backref="assist_player", lazy=True,  foreign_keys='MatchEvent.event_assist_player_id')
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 球员外键
    is_delete = db.Column(db.Boolean, default=False)  # 是否删除

    def __init__(self, name, birthday='',avatar_img='', number=0 , height='', weight='', attendance=0, goals=0, assist=0, soccer_team_id=0, user_id=0):
        self.name = name
        self.birthday = birthday
        self.avatar_img = avatar_img
        self.number = number
        self.height = height
        self.weight = weight
        self.attendance = attendance
        self.goals = goals
        self.assist = assist
        self.soccer_team_id = soccer_team_id
        self.user_id = user_id
