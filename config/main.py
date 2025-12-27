import logging
from core_engine.config import Config
from core_engine.database import Database
from core_engine.models import Base
from core_engine.routes import api

def create_tables(engine):
    Base.metadata.create_all(engine)

def main():
    logging.basicConfig(level=logging.INFO)
    config = Config()
    database = Database(config.db_url)
    engine = database.engine

    create_tables(engine)

    api.run(config.port)

if __name__ == "__main__":
    main()