# AdminUserResource.py api管理，创建所有api类视图对象
from flask_restful import Resource, fields, marshal_with, reqparse, request
from App.Models.AdminUser import *
from App.Apis import result_fields

# 字段格式化
AdminUser_fields = {
    "id": fields.Integer,  # id
    "username": fields.String,  # 用户名
    # 'password': fields.String,  # 密码，不返回
    "email": fields.String,  # 邮箱
    "phone": fields.String,  # 手机号
}


class AdminUserResource(Resource):
    # 查找所有用户
    @marshal_with(result_fields(AdminUser_fields))
    def get(self):
        try:
            user_id = request.args.get('user_id')
            if user_id:
                admin_users = AdminUser.query.get(user_id)
                if admin_users:
                    return {"data": admin_users}
                else:
                    return {"status": 0, "msg": "用户不存在"}
            else:
                admin_users = AdminUser.query.all()
                return {"data": admin_users}
        except Exception as e:
            return {"status": 0, "msg": str(e)}, 500

    # 添加用户
    @marshal_with(result_fields(AdminUser_fields))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("username", type=str, required=True, help="用户名不能为空")
            parser.add_argument("password", type=str, required=True, help="密码不能为空")
            parser.add_argument("email", type=str, required=False, help="邮箱不能为空")
            parser.add_argument("phone", type=str, required=False, help="手机号不能为空")
            args = parser.parse_args()
            admin_user = AdminUser(**args)
            db.session.add(admin_user)
            db.session.commit()
            return {"data": admin_user}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

    # 删除用户
    @marshal_with(result_fields(AdminUser_fields))
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int, required=True, help="id不能为空")
            args = parser.parse_args()
            admin_user = AdminUser.query.get(args["id"])
            db.session.delete(admin_user)
            db.session.commit()
            return {"data": admin_user}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500

    # 修改用户，允许只修改一个字段
    @marshal_with(result_fields(AdminUser_fields))
    def put(self):
        try:
            parser = (
                reqparse.RequestParser()
            )  # 创建参数解析器，因每个服务的要求的参数不同，所以每个服务都需要创建一个参数解析器
            parser.add_argument("id", type=int, required=True, help="id不能为空")  # 添加参数
            parser.add_argument("username", type=str, required=False, help="用户名不能为空")
            parser.add_argument("password", type=str, required=False, help="密码不能为空")
            parser.add_argument("email", type=str, required=False, help="邮箱不能为空")
            parser.add_argument("phone", type=str, required=False, help="手机号不能为空")
            args = parser.parse_args()  # 解析参数
            admin_user = AdminUser.query.get(args["id"])  # 获取要修改的用户
            for k, v in args.items():  # 遍历参数
                if v:  # 如果参数不为空
                    setattr(admin_user, k, v)  # 修改用户属性
            db.session.commit()
            return {"data": admin_user}
        except Exception as e:
            # 回滚数据库
            db.session.rollback()
            return {"status": 0, "msg": str(e)}, 500
