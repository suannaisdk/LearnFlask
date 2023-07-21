# urls.py 描述了路由规则
from .exts import api    # 导入api插件
from .apis import *      # 导入api中创建的视图

api.add_resource(HelloResource, '/hello')   # 添加路由规则，将Hello类视图添加到路由中
api.add_resource(AdminUserResource, '/adminUser')   # 添加路由规则，将AdminUser类视图添加到路由中
