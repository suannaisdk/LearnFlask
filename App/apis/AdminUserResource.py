# AdminUserResource.py api管理，创建所有api类视图对象
from flask_restful import Resource, fields, marshal_with, reqparse
from App.Models.AdminUser import *


# 返回字段格式化
def result_fields(data):
    ret_fields = {
        'status': fields.Integer,  # 返回状态码，1表示成功，0表示失败
        'msg': fields.String(default='success'),  # 返回信息
        'data': fields.List(fields.Nested(data))  # 返回数据
    }
    return ret_fields


# 字段格式化
AdminUser_fields = {
    'id': fields.Integer,  # id
    'username': fields.String,  # 用户名
    # 'password': fields.String,  # 密码，不返回
    'email': fields.String,  # 邮箱
    'phone': fields.String,  # 手机号
}


class AdminUserResource(Resource):
    # 查找所有用户
    @marshal_with(result_fields(AdminUser_fields))
    def get(self):
        try:
            adminUsers = AdminUser.query.all()
            return {'data': adminUsers}
        except Exception as e:
            return {'status': 0, 'msg': str(e)}

    # 添加用户
    @marshal_with(result_fields(AdminUser_fields))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, required=True, help='用户名不能为空')
            parser.add_argument('password', type=str, required=True, help='密码不能为空')
            parser.add_argument('email', type=str, required=True, help='邮箱不能为空')
            parser.add_argument('phone', type=str, required=True, help='手机号不能为空')
            args = parser.parse_args()
            admin_user = AdminUser(**args)
            db.session.add(admin_user)
            db.session.commit()
            return {'data': admin_user}
        except Exception as e:
            return {'status': 0, 'msg': str(e)}
