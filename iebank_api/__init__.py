from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from config import ProductionConfig
from flask_cors import CORS
import os

app = Flask(__name__)

# Select environment based on the ENV environment variable
if os.getenv('ENV') == 'local':
    print("Running in local mode")
    app.config.from_object('config.LocalConfig')
elif os.getenv('ENV') == 'dev':
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')
elif os.getenv('ENV') == 'ghci':
    print("Running in github CI mode")
    app.config.from_object('config.GithubCIConfig')

db = SQLAlchemy(app)

from iebank_api.models import Account

with app.app_context():
    #query = text("ALTER TABLE account ADD COLUMN country VARCHAR(32)")
    #db.session.execute(query)
    #db.session.commit()
    db.create_all()
CORS(app)

from iebank_api import routes
