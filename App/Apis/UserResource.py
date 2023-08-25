from flask_restful import Resource, fields, marshal_with, reqparse
from App.Models.AdminUser import *
from App.Apis import result_fields
from App.Models.User import User

# 字段格式化
user_fields = {
    "id": fields.Integer,  # id
    "username": fields.String,  # 用户名
    # 'password': fields.String,  # 密码，不返回
    "is_admin": fields.Boolean,  # 是否是管理员
    "soccer_player_id": fields.Integer,  # 球员外键
}
class UserResource(Resource):
    @marshal_with(result_fields(user_fields))
    def get(self, user_id=None):
        try:
            if user_id:
                users = User.query.get(user_id)
                if users:
                    return {"data": users}
                else:
                    return {"status": 0, "msg": "用户不存在"},500
            else:
                users = User.query.all()
                return {"data": users}
        except Exception as e:
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(user_fields))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("username", type=str, required=True, help="用户名不能为空")
            parser.add_argument("password", type=str, required=True, help="密码不能为空")
            parser.add_argument(
                "soccer_player_id", type=int, required=False, help="球员外键"
            )
            args = parser.parse_args()
            user = User(**args)
            db.session.add(user)
            db.session.commit()
            return {"data": user}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(user_fields))
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int, required=True, help="id不能为空")
            parser.add_argument("username", type=str, required=True, help="用户名不能为空")
            parser.add_argument("password", type=str, required=True, help="密码不能为空")
            parser.add_argument(
                "soccer_player_id", type=int, required=False, help="球员外键"
            )
            args = parser.parse_args()
            user = User.query.get(args["id"])
            user.username = args["username"]
            user.password = args["password"]
            user.soccer_player_id = args["soccer_player_id"]
            db.session.commit()
            return {"data": user}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

    @marshal_with(result_fields(user_fields))
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int, required=True, help="id不能为空")
            args = parser.parse_args()
            user = User.query.get(args["id"])
            db.session.delete(user)
            db.session.commit()
            return {"data": user}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

class UserLogin(Resource):
    @marshal_with(result_fields(user_fields))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("username", type=str, required=True, help="用户名不能为空")
            parser.add_argument("password", type=str, required=True, help="密码不能为空")
            args = parser.parse_args()
            # 通过username获取到用户名，然后再通过用户名获取到用户信息
            user = User.query.filter_by(username=parser.parse_args()["username"]).first()
            if user:        # 如果用户存在
                if user.password == args["password"]:   # 如果密码正确
                    return {"data": user}
                else:
                    return {"status": 0, "msg": "用户名或密码错误"}
            else:
                return {"status": 0, "msg": "用户不存在"}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500