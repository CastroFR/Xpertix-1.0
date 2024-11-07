import os

#class Configuracion:
#    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/xpertix_db'
#    SECRET_KEY = 'clave_secreta_super_segura'
#    SQLALCHEMY_TRACK_MODIFICATIONS = False



class Configuracion:
#    """Clase de configuración de la aplicación."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_super_segura'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/xpertix_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
