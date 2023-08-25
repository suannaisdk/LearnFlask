from flask_restful import fields


def result_fields(data):
    ret_fields = {
        'status': fields.Integer(default=1),  # 返回状态码，1表示成功，0表示失败
        'msg': fields.String(default='success'),  # 返回信息
        'data': fields.List(fields.Nested(data))  # 返回数据
    }
    return ret_fields
