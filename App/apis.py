# apis.py api管理，创建所有api类视图对象
from flask_restful import Resource


# 创建一个类视图HelloWorld
class HelloResource(Resource):
    def get(self):
        return {"msg": "hello world"}
