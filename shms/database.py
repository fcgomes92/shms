from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, configure_mappers


class Database(object):
    _session = None
    _database = None
    _engine = None

    def __init__(self, database_url):
        self.set_session(database_url)
        self.map_models()

    def set_session(self, database_url):
        if not self._engine:
            self._engine = create_engine(database_url, convert_unicode=True)
        self._session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=self._engine))

        return self._session

    def commit_session(self, exception=None):
        if exception:
            self._session.rollback()
        else:
            self._session.commit()
        self._session.remove()

        if hasattr(self._engine, 'dispose'):
            self._engine.dispose()

    def session(self):
        return self._session

    def map_models(self):
        import shms.models
        shms.models.BaseModel.metadata.create_all(bind=self._engine)
        # maps the abstract user class
        configure_mappers()
