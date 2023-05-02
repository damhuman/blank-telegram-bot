import logging

from services.singleton import SingletonMeta
from .base import session, current_session
from database.models.user import User, Role


logger = logging.getLogger(__name__)


# DEPRECATED
class DbConnector(metaclass=SingletonMeta):
    """
        Database abstraction
    """

    def __init__(self):
        self.Session = current_session

    def get_or_create_user(self, telegram_id, username=None):
        with session() as s:
            res = s.query(User).filter(User.telegram_id == telegram_id).first()
            if res is None:
                user = User(telegram_id=telegram_id, username=username)
                s.add(user)
                s.commit()
                res = user

        return res

    def update_user(self, user: User):
        with session() as s:
            res = s.query(User).filter(User.telegram_id == user.telegram_id).first()

            res.is_banned = user.is_banned
            res.username = user.username
            res.email = user.email
            res.role_id = user.role_id
            res.language = user.language

        return True
