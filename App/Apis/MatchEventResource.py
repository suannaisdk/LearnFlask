import datetime
from flask_restful import Resource, fields, marshal_with, reqparse, request
from App.Apis import result_fields
from App.Models.MatchEvent import *
from App.Models.SoccerPlayer import SoccerPlayer
from App.Models.SoccerMatch import SoccerMatch

# 字段格式化
MatchEvent_fields = {
    "id": fields.Integer,  # id
    "match_id": fields.Integer(attribute='event.id'),
    "event_time": fields.DateTime(dt_format="iso8601"),  # 事件时间
    "event_team_id": fields.Integer(),  # 事件时间
    "event_goal_player_id": fields.Integer(),  # 进球队员
    "event_goal_player_name": fields.String(attribute='goal_player.name'),  # 进球队员
    "event_assist_player_id": fields.Integer(),  # 助攻队员
    "event_assist_player_name": fields.String(attribute='assist_player.name'),  # 助攻队员
}


class MatchEventResource(Resource):
    @marshal_with(result_fields(MatchEvent_fields))
    def get(self):
        try:
            event_id = request.args.get('event_id')
            if event_id:
                event = MatchEvent.query.get(event_id)
                if event:
                    return {"data": event}
                else:
                    return {"status": 0, "msg": "事件不存在"}
            else:
                events = MatchEvent.query.all()
                return {"data": events}
        except Exception as e:
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(MatchEvent_fields))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('match_id', type=int, required=True, help="比赛id不能为空")
            parser.add_argument('event_time', type=str, required=True, help="事件时间设置异常")
            parser.add_argument('event_team_id', type=int, required=True, help="队伍设置异常")
            parser.add_argument('event_goal_player_id', type=int, required=False, help="进球球员设置异常")
            parser.add_argument('event_assist_player_id', type=int, required=False, help="助攻球员设置异常")
            args = parser.parse_args()
            args["event_time"] = datetime.datetime.strptime(
                args["event_time"], "%Y-%m-%d %H:%M:%S"
            )
            print(args["event_time"], args.get('event_goal_player_id'))
            event = MatchEvent(**args)
            # 修改soccer_player中的进球数
            if args["event_goal_player_id"]:
                goal_player = SoccerPlayer.query.get(args.get('event_goal_player_id'))
                if goal_player:
                    goal_player.goals += 1
                    db.session.add(goal_player)

            # 修改soccer_player中的助攻数量
            if args["event_assist_player_id"]:
                assist_player = SoccerPlayer.query.get(args.get('event_assist_player_id'))
                if assist_player:
                    assist_player.assist += 1
                    db.session.add(assist_player)
            # 修改队伍进球
            if args['event_team_id']:
                match = SoccerMatch.query.get(args.get('match_id'))
                if match.home_team_id == args.get('event_team_id'):
                    match.home_goals += 1
                elif match.guest_team_id == args.get('event_team_id'):
                    match.guest_goals += 1
                else:
                    print('队伍错误！')
                db.session.add(match)

            db.session.add(event)
            db.session.commit()
            return {"data": event}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(MatchEvent_fields))
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, required=True, help="事件id不能为空")
            parser.add_argument('match_id', type=int, required=False, help="比赛id不能为空")
            parser.add_argument('event_time', type=str, required=False, help="事件时间设置异常")
            parser.add_argument('event_team_id', type=int, required=False, help="队伍设置异常")
            parser.add_argument('event_goal_player_id', type=int, required=False, help="进球球员设置异常")
            parser.add_argument('event_assist_player_id', type=int, required=False, help="助攻球员设置异常")
            args = parser.parse_args()
            if args.get("event_time"):
                args["event_time"] = datetime.datetime.strptime(args["event_time"], "%Y-%m-%d %H:%M:%S")
            event = MatchEvent.query.get(args.get("id"))
            if event:
                for k, v in args.items():
                    if v:
                        setattr(event, k, v)

                db.session.add(event)
                db.session.commit()
                return {"data": event}
            else:
                return {"status": 0, "msg": "事件不存在"}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(MatchEvent_fields))
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=int, required=True, help="事件id不能为空")
            args = parser.parse_args()
            event = MatchEvent.query.get(args.get("id"))
            if event:
                db.session.delete(event)
                db.session.commit()
                return {"data": event}
            else:
                return {"status": 0, "msg": "事件不存在"}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500
