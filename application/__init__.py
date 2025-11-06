from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus

# Vamos iniciar o pé por aqui, Let's start the foot here



password = quote_plus("12345678")#

def create_app():
    app = Flask(__name__)

    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://Cad_for_users:{password}@localhost/usersdb'

    global engine, SessionLocal, Base
    Base = declarative_base()
    #   engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

    engine = create_engine(
    f"mysql+mysqlconnector://CompleteUser:{password}@localhost:3307/usersdb",
  
    )

    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    from . import routes
    routes.init_routes(app)

    return app