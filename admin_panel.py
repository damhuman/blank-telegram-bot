from flask import Flask
from flask_admin import Admin
from flask_basicauth import BasicAuth

from configuration import (DB_URL, ADMIN_PANEL_SECRET_KEY,
                           ADMIN_PANEL_BASIC_AUTH_USERNAME,
                           ADMIN_PANEL_BASIC_AUTH_PASSWORD, ADMIN_PANEL_NAME)


from database.models.user import (User, Role, UserView, RoleView)
from database.base import current_session

admin_panel_app = Flask(__name__)
admin = Admin(admin_panel_app, name=ADMIN_PANEL_NAME, template_mode='bootstrap3', url='/admin_panel/')

admin_panel_app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
admin_panel_app.config['SECRET_KEY'] = ADMIN_PANEL_SECRET_KEY
admin_panel_app.config['BASIC_AUTH_USERNAME'] = ADMIN_PANEL_BASIC_AUTH_USERNAME
admin_panel_app.config['BASIC_AUTH_PASSWORD'] = ADMIN_PANEL_BASIC_AUTH_PASSWORD
admin_panel_app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(admin_panel_app)

# user tables
admin.add_view(UserView(User, current_session))
admin.add_view(RoleView(Role, current_session))

if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer

    http_server = WSGIServer(('', 4000), admin_panel_app)
    http_server.serve_forever()
