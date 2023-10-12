from App.exts import db  # 导入sqlalchemy插件


class SoccerPlayer(db.Model):
    __tablename__ = 'soccer_player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    name = db.Column(db.String(20), nullable=False)  # 姓名
    # birthday = db.Column(db.DateTime, nullable=False)  # 生日
    avatar_img = db.Column(db.Text(), nullable=True)  # 头像
    height = db.Column(db.Float, nullable=True)  # 身高
    weight = db.Column(db.Float, nullable=True)  # 体重
    goals = db.Column(db.Integer, nullable=True)  # 进球数
    assist = db.Column(db.Integer, nullable=True)  # 助攻数
    soccer_team_id = db.Column(db.Integer, db.ForeignKey('soccer_team.id'))  # 球队外键，外键写在多的一方
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 球员外键
    is_delete = db.Column(db.Boolean, default=False)  # 是否删除

    def __init__(self, name, avatar_img='', height='', weight='', goals=0, assist=0, soccer_team_id=0, user_id=0):
        self.name = name
        self.avatar_img = avatar_img
        self.height = height
        self.weight = weight
        self.goals = goals
        self.assist = assist
        self.soccer_team_id = soccer_team_id
        self.user_id = user_id
