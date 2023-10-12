app.py 是主程序，入口文件
App文件夹
    __init__.py 描述了App的初始化规则
    urls.py 描述了路由规则
    apis.py 描述了接口规则
    exts.py 描述了插件规则
    models.py 描述了数据库模型规则。


## 部署：
### 1、下载代码，安装nginx和gunicorn
### 2、nginx配置
### 3、gunicorn配置，gunicorn -b 0.0.0.0:8000 app:app -D 后台部署
### 4、查看gunicorn id ps aux | grep gunicorn
### 5、配置数据库，flask db init \ flask db migrate \ flask db upgrade