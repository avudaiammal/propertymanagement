import connexion
import os

basedir = os.path.abspath(os.path.dirname(__file__))
application = connexion.FlaskApp(__name__)
application.add_API("swagger.yaml")
app = application.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'db.sqlite')
