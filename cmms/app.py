from flask import Flask
from settings import Configuration
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from turbo_flask import Turbo
#from sqlalchemy.orm import Query

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

app = Flask(__name__)
app.config.from_object(Configuration)
turbo = Turbo(app)

# db = SQLAlchemy(app)
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app=app, metadata=metadata)


import migrates

migrate = Migrate(app, db, render_as_batch=True)
