from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix" : 'ix_%(column_0_label)s',
    "uq" : "uq_%(table_name)s_%(column_0_name)s",
    "ck" : "ck_%(table_name)s_%(column_0_name)s",
    "fk" : "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk" : "pk_%(table_name)s"
    }
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()
# 위의 수정 내용: SQLite 데이터 베이스 플라스크 ORM 에서 정상으로 사용하기 위한것.



def create_app():
    app = Flask(__name__)
    # to read written list in config.py
    app.config.from_object(config)

    # ORM
    db.init_app(app)    # enroll in app
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # blueprint 등록

    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime


    return app