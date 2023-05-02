import json

from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Column, BigInteger, String, Integer, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship

from bot.utils.constants import ADMIN_PANEL_PAGE_SIZE, Language, DEFAULT_LANGUAGE
from database.base import Base


class User(Base):
    __tablename__ = 'users'
    telegram_id = Column(BigInteger, primary_key=True)
    username = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    role_id = Column(Integer(), ForeignKey('roles.id'), nullable=True)
    is_banned = Column(Boolean(), default=False)
    language = Column(Enum(Language), default=DEFAULT_LANGUAGE)
    # relationship
    role = relationship('Role', backref='users')

    def __repr__(self):
        return f'< Username: {self.username}, Telegram Id: {self.telegram_id} >'

    def to_json(self):
        return json.dumps({
            "telegram_id": self.telegram_id,
            "username": self.username,
            "is_banned": self.is_banned,
            "email": self.email,
            "role_id": self.role_id,
            "language": self.language
        })

    @staticmethod
    def from_json(data):
        data = json.loads(data)
        return User(
            telegram_id=data['telegram_id'],
            username=data['username'],
            is_banned=data['is_banned'],
            email=data['email'],
            discord_account=data['discord_account'],
            role_id=data['role_id'],
            language=data['language'],
        )


class UserView(ModelView):
    column_list = ('telegram_id', 'username', 'email', 'role', 'is_banned', 'language')
    form_columns = ['telegram_id', 'username', 'email', 'role', 'is_banned', 'language']
    column_searchable_list = ['username', 'telegram_id', 'email', 'language']
    column_filters = ['username', 'role', 'telegram_id', 'email', 'language']
    page_size = ADMIN_PANEL_PAGE_SIZE


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    can_manage_users = Column(Boolean(), default=False)

    def __repr__(self):
        return f'< Role: {self.name}, Id: {self.id} >'


class RoleView(ModelView):
    column_list = ('id', 'name', 'can_manage_users',)
    form_columns = ['name', 'can_manage_users']
    column_searchable_list = ['name']
    column_filters = ['name', 'can_manage_users']
    page_size = ADMIN_PANEL_PAGE_SIZE
