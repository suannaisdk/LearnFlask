from App.exts import db  # 导入sqlalchemy插件


class SoccerPlayer(db.Model):
    __tablename__ = 'soccer_player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键
    name = db.Column(db.String(20), nullable=False)  # 姓名
    # birthday = db.Column(db.DateTime, nullable=False)  # 生日
    avatar_img = db.Column(db.Text(), nullable=False)  # 头像
    height = db.Column(db.Float, nullable=False)  # 身高
    weight = db.Column(db.Float, nullable=False)  # 体重
    goals = db.Column(db.Integer, nullable=False)  # 进球数
    assist = db.Column(db.Integer, nullable=False)  # 助攻数
    soccer_team_id = db.Column(db.Integer, db.ForeignKey('soccer_team.id'))  # 球队外键，外键写在多的一方
    is_delete = db.Column(db.Boolean, default=False)  # 是否删除