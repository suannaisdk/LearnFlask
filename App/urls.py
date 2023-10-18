# urls.py 描述了路由规则
from .exts import api    # 导入api插件
from App.Apis.HelloResource import HelloResource      # 导入api中创建的视图
from App.Apis.AdminUserResource import AdminUserResource      # 导入api中创建的视图
from App.Apis.SoccerPlayerResource import SoccerPlayerResource      # 导入api中创建的视图
from App.Apis.SoccerTeamResource import SoccerTeamResource      # 导入api中创建的视图
from App.Apis.SoccerMatchResource import SoccerMatchResource      # 导入api中创建的视图
from App.Apis.UserResource import UserResource, UserLogin      # 导入api中创建的视图
from App.Apis.MatchEventResource import MatchEventResource          # 导入api中比赛事件

api.add_resource(HelloResource, '/')   # 添加路由规则，将Hello类视图添加到路由中
# 添加路由规则，将AdminUser类视图添加到路由中
api.add_resource(AdminUserResource, '/admin_users', '/admin_users/', '/admin_users/<int:user_id>')
# 添加路由规则，将SoccerPlayer类视图添加到路由中
api.add_resource(SoccerPlayerResource, '/soccer_players', '/soccer_players/', '/soccer_players/<int:player_id>')
api.add_resource(SoccerTeamResource, '/soccer_teams', '/soccer_teams/', '/soccer_teams/<int:team_id>')
api.add_resource(SoccerMatchResource, '/soccer_matches', '/soccer_matches/', '/soccer_matches/<int:match_id>')
api.add_resource(UserResource, '/users', '/users/', '/users/<int:user_id>')
api.add_resource(UserLogin, '/login', '/login/')
api.add_resource(MatchEventResource, '/match_events', '/match_events/','/match_events/<int:event_id>')
