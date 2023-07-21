from flask_restful import Resource
# 创建一个类视图HelloWorld


class HelloResource(Resource):
    def get(self):
        return {"msg": "hello world"}