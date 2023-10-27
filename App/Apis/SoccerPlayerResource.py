# SoccerPlayerResource.py api管理，创建所有api类视图对象
from flask_restful import Resource, fields, marshal_with, reqparse, request
from App.Apis import result_fields
from App.Models.SoccerPlayer import *
from App.Apis.MatchEventResource import MatchEvent_fields

# 字段格式化
SoccerPlayer_fields = {
    'id': fields.Integer,  # id
    'name': fields.String,  # 姓名
    'birthday': fields.String,  # 生日
    'avatar_img': fields.String,  # 头像
    'number': fields.Integer,  # 号码
    'height': fields.Float,  # 身高
    'weight': fields.Float,  # 体重
    'attendance': fields.Integer,  # 出场次数
    'goals': fields.Integer,  # 进球数
    'assist': fields.Integer,  # 助攻数
    'soccer_team_id': fields.Integer(attribute='team.id'),
    # 'goals_events': fields.List(fields.Nested(MatchEvent_fields)),  # 用户的所有动作
    # 'assist_events': fields.List(fields.Nested(MatchEvent_fields)),  # 用户的所有动作
    'user_id': fields.Integer(attribute='user.id'),
    'soccer_team': fields.String(attribute='team.team_name'),
    # 球队外键。attribute指定外键的字段名，team是在SoccerTeam.py中定义的relationship，其中backref='team'，所以这里可以用team.team_name
}


class SoccerPlayerResource(Resource):
    @marshal_with(result_fields(SoccerPlayer_fields))
    def get(self, player_id=None):
        try:
            player_id = request.args.get('player_id')
            if player_id:
                players = SoccerPlayer.query.get(player_id)
                if players:
                    return {'data': players}
                else:
                    return {'status': 0, 'msg': '球员不存在'}
            else:
                players = SoccerPlayer.query.all()
                return {'data': players}
        except Exception as e:
            return {'status': 0, 'msg': str(e)},500

    @marshal_with(result_fields(SoccerPlayer_fields))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_id', type=int, required=True, help='用户id设置异常')
            parser.add_argument('name', type=str, required=True, help='姓名不能为空')
            parser.add_argument('birthday', type=str, help='生日不能为空')
            parser.add_argument('avatar_img', type=str, required=False, help='头像设置异常')
            parser.add_argument('number', type=int, required=False, help='号码设置异常')
            parser.add_argument('height', type=float, required=False, help='身高设置异常')
            parser.add_argument('weight', type=float, required=False, help='体重设置异常')
            parser.add_argument('attendance', type=int, required=False, help='出场数设置异常')
            parser.add_argument('goals', type=int, required=False, help='进球数设置异常')
            parser.add_argument('assist', type=int, required=False, help='助攻数设置异常')
            parser.add_argument('soccer_team_id', type=int, required=False, help='球队id设置异常')
            args = parser.parse_args()
            player = SoccerPlayer(**args)
            db.session.add(player)
            db.session.commit()
            return {'data': player}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {'status': 0, 'msg': str(e)}, 500

    @marshal_with(result_fields(SoccerPlayer_fields))
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, required=True, help='id不能为空')
            parser.add_argument('user_id', type=int, required=False, help='用户id设置异常')
            parser.add_argument('name', type=str, required=False, help='姓名不能为空')
            parser.add_argument('birthday', type=str, required=False, help='生日不能为空')
            parser.add_argument('avatar_img', type=str, required=False, help='头像设置异常')
            parser.add_argument('number', type=int, required=False, help='号码设置异常')
            parser.add_argument('height', type=float, required=False, help='身高设置异常')
            parser.add_argument('weight', type=float, required=False, help='体重设置异常')
            parser.add_argument('attendance', type=int, required=False, help='出场数设置异常')
            parser.add_argument('goals', type=int, required=False, help='进球数设置异常')
            parser.add_argument('assist', type=int, required=False, help='助攻数设置异常')
            parser.add_argument('soccer_team_id', type=int, required=False, help='球队id设置异常')
            args = parser.parse_args()
            player = SoccerPlayer.query.get(args.get('id'))
            if player:
                for k, v in args.items():
                    if v:
                        setattr(player, k, v)
                db.session.commit()
                return {'data': player}
            else:
                return {'status': 0, 'msg': '球员不存在'}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {'status': 0, 'msg': str(e)}, 500

    @marshal_with(result_fields(SoccerPlayer_fields))
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, required=True, help='id不能为空')
            args = parser.parse_args()
            player = SoccerPlayer.query.get(args['id'])
            if player:
                db.session.delete(player)
                db.session.commit()
                return {'data': player}
            else:
                return {'status': 0, 'msg': '球员不存在'}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {'status': 0, 'msg': str(e)}, 500
        # 将删除改为逻辑删除，将is_delete字段改为True
        # try:
        #     parser = reqparse.RequestParser()
        #     parser.add_argument('id', type=int, required=True, help='id不能为空')
        #     args = parser.parse_args()
        #     player = SoccerPlayer.query.get(args['id'])
        #     player.is_delete = True
        #     db.session.commit()
        #     return {'data': player}
        # except Exception as e:
        #     # 回滚数据库
        #     db.session.rollback()
        #     return {'status': 0, 'msg': str(e)}, 500
