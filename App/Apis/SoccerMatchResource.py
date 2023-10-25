# SoccerMatchResource.py api管理，创建所有api类视图对象
import datetime
from flask_restful import Resource, fields, marshal_with, reqparse, request
from App.Apis import result_fields
from App.Models.SoccerMatch import *
from App.Apis.MatchEventResource import MatchEvent_fields

# 字段格式化
SoccerMatch_fields = {
    "id": fields.Integer,  # id
    "home_team_id": fields.Integer(attribute='home_team.id'),  # 主队外键
    "home_team_name": fields.String(attribute='home_team.team_name'),  # 主队外键
    "home_team_logo": fields.String(attribute='home_team.logo_img_url'),  # 主队外键
    "guest_team_id": fields.Integer(attribute='guest_team.id'),  # 客队外键
    "guest_team_name": fields.String(attribute='guest_team.team_name'),  # 客队外键
    "guest_team_logo": fields.String(attribute='guest_team.logo_img_url'),  # 客队外键
    "match_time": fields.DateTime(dt_format="iso8601"),  # 比赛时间
    "match_address": fields.String,  # 比赛地点
    "match_content": fields.String,  # 比赛简介
    "match_status": fields.Integer,  # 比赛状态，0未开始，1比赛开始，2比赛结束
    "match_events": fields.List(fields.Nested(MatchEvent_fields)),  # 查看比赛中所有事件
    "home_goals": fields.Integer,  # 主队进球数
    "guest_goals": fields.Integer,  # 客队进球数
    # 'is_delete': fields.Boolean  # 是否删除
}


class SoccerMatchResource(Resource):
    @marshal_with(result_fields(SoccerMatch_fields))
    def get(self):
        try:
            match_id = request.args.get('match_id')
            if match_id:
                match = SoccerMatch.query.get(match_id)
                if match:
                    return {"data": match}
                else:
                    return {"status": 0, "msg": "比赛不存在"}
            else:
                matches = SoccerMatch.query.all()
                return {"data": matches}
        except Exception as e:
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(SoccerMatch_fields))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "home_team_id", type=int, required=True, help="主队id不能为空"
            )
            parser.add_argument(
                "guest_team_id", type=int, required=True, help="客队id不能为空"
            )
            parser.add_argument("match_time", type=str, required=False, help="比赛时间设置异常")
            parser.add_argument(
                "match_address", type=str, required=False, help="比赛地点设置异常"
            )
            parser.add_argument(
                "match_content", type=str, required=False, help="比赛简介设置异常"
            )
            parser.add_argument(
                "match_status", type=int, required=False, help="比赛状态设置异常"
            )
            parser.add_argument(
                "home_goals", type=int, required=False, help="主队进球数设置异常"
            )
            parser.add_argument(
                "guest_goals", type=int, required=False, help="客队进球数设置异常"
            )
            args = parser.parse_args()
            args["match_time"] = datetime.datetime.strptime(
                args["match_time"], "%Y-%m-%d %H:%M"
            )
            match = SoccerMatch(**args)
            db.session.add(match)
            db.session.commit()
            return {"data": match}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(SoccerMatch_fields))
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int, required=True, help="id不能为空")
            parser.add_argument(
                "home_team_id", type=int, required=False, help="主队id不能为空"
            )
            parser.add_argument(
                "guest_team_id", type=int, required=False, help="客队id不能为空"
            )
            parser.add_argument("match_time", type=str, required=False, help="比赛时间设置异常")
            parser.add_argument(
                "match_address", type=str, required=False, help="比赛地点设置异常"
            )
            parser.add_argument(
                "match_content", type=str, required=False, help="比赛简介设置异常"
            )
            parser.add_argument(
                "match_status", type=int, required=False, help="比赛状态设置异常"
            )
            parser.add_argument(
                "home_goals", type=int, required=False, help="主队进球数设置异常"
            )
            parser.add_argument(
                "guest_goals", type=int, required=False, help="客队进球数设置异常"
            )
            args = parser.parse_args()
            if args.get("match_time"):
                args["match_time"] = datetime.datetime.strptime(
                    args["match_time"], "%Y-%m-%d %H:%M"
                )
            match = SoccerMatch.query.get(args.get("id"))  # 获取要修改的比赛对象
            # print('test', args["match_status"])
            if match:
                for k, v in args.items():
                    if v:
                        setattr(match, k, v)
                db.session.add(match)
                db.session.commit()
                return {"data": match}
            else:
                return {"status": 0, "msg": "比赛不存在"}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(SoccerMatch_fields))
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int, required=True, help="id不能为空")
            args = parser.parse_args()
            match = SoccerMatch.query.get(args.get("id"))  # 获取要删除的比赛对象
            if match:
                db.session.delete(match)
                db.session.commit()
                return {"data": match}
            else:
                return {"status": 0, "msg": "比赛不存在"}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500
