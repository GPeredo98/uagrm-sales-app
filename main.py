from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy_utils import database_exists
from utilities import database, schemas
from controllers.productos import productos
from controllers.ventas import ventas
import os
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "UAGRM Aplicación de ventas"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###
app.config.from_pyfile(os.path.join('environments', 'settings.py'))
app.register_blueprint(productos, url_prefix='/productos')
app.register_blueprint(ventas, url_prefix='/ventas')
CORS(app)
# api = Api(app)
if database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    database.init_app(app)
    schemas.init_app(app)
    with app.app_context():
        database.create_all()
else:
    raise Exception("Database not found")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"