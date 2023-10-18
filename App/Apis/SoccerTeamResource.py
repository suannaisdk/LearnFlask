from flask_restful import Resource, fields, marshal_with, reqparse, request
from App.Models.SoccerTeam import *
from App.Apis import result_fields
from App.Apis.SoccerPlayerResource import SoccerPlayer_fields
from App.Apis.SoccerMatchResource import SoccerMatch_fields
# 字段格式化
SoccerTeam_fields = {
    'id': fields.Integer,  # id
    'team_name': fields.String,  # 球队名
    'content': fields.String,  # 球队简介
    'home_matches': fields.List(fields.Nested(SoccerMatch_fields)),  # 比赛外键
    'guest_matches': fields.List(fields.Nested(SoccerMatch_fields)),  # 比赛外键
    'soccer_players': fields.List(fields.Nested(SoccerPlayer_fields)),  # 球员外键
    'is_delete': fields.Boolean,  # 是否删除
}


class SoccerTeamResource(Resource):
    @marshal_with(result_fields(SoccerTeam_fields))
    def get(self):
        team_id = request.args.get('team_id')
        try:
            if team_id:
                teams = SoccerTeam.query.get(team_id)
                if teams:
                    return {'data': teams}
                else:
                    return {'status': 0, 'msg': '球队不存在'}
            else:
                teams = SoccerTeam.query.all()
                return {'data': teams}
        except Exception as e:
            return {'status': 0, 'msg': str(e)}, 500

    @marshal_with(result_fields(SoccerTeam_fields))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('team_name', type=str, required=True, help='球队名不能为空')
            parser.add_argument('content', type=str, required=False, help='球队简介设置异常')
            args = parser.parse_args()
            team = SoccerTeam(**args)
            db.session.add(team)
            db.session.commit()
            return {'data': team}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {'status': 0, 'msg': str(e)}, 500

    @marshal_with(result_fields(SoccerTeam_fields))
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, required=True, help='id不能为空')
            parser.add_argument('team_name', type=str, required=False, help='球队名不能为空')
            parser.add_argument('content', type=str, required=False, help='球队简介设置异常')
            args = parser.parse_args()
            team = SoccerTeam.query.get(args['id'])
            if team:
                for key,value in args.items():
                    if value:
                        setattr(team, key, value)
                # team.team_name = args['team_name']
                # team.content = args['content']
                db.session.commit()
                return {'data': team}
            else:
                return {'status': 0, 'msg': '球队不存在'}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {'status': 0, 'msg': str(e)}, 500

    @marshal_with(result_fields(SoccerTeam_fields))
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, required=True, help='id不能为空')
            args = parser.parse_args()
            team = SoccerTeam.query.get(args['id'])
            if team:
                db.session.delete(team)
                db.session.commit()
                return {'data': team}
            else:
                return {'status': 0, 'msg': '球队不存在'}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {'status': 0, 'msg': str(e)}, 500
        # 逻辑删除
        # try:
        #     parser = reqparse.RequestParser()
        #     parser.add_argument('id', type=int, required=True, help='id不能为空')
        #     args = parser.parse_args()
        #     team = SoccerTeam.query.get(args['id'])
        #     team.is_delete = True
        #     db.session.commit()
        #     return {'data': team}
        # except Exception as e:
        #     # 回滚数据库
        #     db.session.rollback()
        #     return {'status': 0, 'msg': str(e)}, 500
