from flask import Flask
from server.extentions import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import SQLALCHEMY_DATABASE_URI, JWT_SECRET_KEY

migrate = Migrate()
jwt = JWTManager()


from server.controllers.auth_controller import auth_controller
from server.controllers.episode_controller import episode_controller
from server.controllers.appearance_controller import appearance_controller
from server.controllers.guest_controller import guest_controller  

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY  

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_controller)
    app.register_blueprint(episode_controller)
    app.register_blueprint(appearance_controller)
    app.register_blueprint(guest_controller) 

 
    from server.models import user, guest, episode, appearance

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
