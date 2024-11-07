from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

db = SQLAlchemy()

def crear_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/xpertix_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'clave_secreta'
    
    # Inicialización de extensiones
    db.init_app(app)
    
    # Configuración de Flask-Login
    #login_manager = LoginManager()
    #login_manager.init_app(app)
    #login_manager.login_view = 'auth.login'

    # Importar modelos
    #from app.modelos import Usuario

    # Definir user_loader para Flask-Login
    #@login_manager.user_loader
    #def cargar_usuario(usuario_id):
    #    return Usuario.query.get(int(usuario_id))
    
    # Registro de blueprints
    #from app.auth import auth_blueprint
    #app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.rutas import principal
    app.register_blueprint(principal)
    
    return app
