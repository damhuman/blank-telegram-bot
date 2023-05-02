import logging
import typing
from contextlib import contextmanager

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker, scoped_session

from configuration import DB_URL

Session = sessionmaker(expire_on_commit=False)
engine = create_engine(DB_URL, pool_size=15, max_overflow=30)
metadata = MetaData(bind=engine)
current_session = scoped_session(Session)

logger = logging.getLogger(__name__)


@contextmanager
def session(**kwargs) -> typing.ContextManager[Session]:
    """Provide a transactional scope around a series of operations."""
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception as e:
        logger.error(str(e))
        new_session.rollback()
        raise
    finally:
        new_session.close()


@as_declarative(metadata=metadata)
class Base:
    pass
