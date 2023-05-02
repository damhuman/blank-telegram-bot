import typing

from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from aiogram.types.base import TelegramObject

from bot.utils.constants import ADMIN


class PermissionsFilter(BoundFilter):
    key = 'permissions'

    def __init__(self, permissions: typing.Union[None, str, typing.Collection[str]] = None):
        if permissions is None:
            self.required_permissions = None
        elif isinstance(permissions, str):
            self.required_permissions = {permissions}
        else:
            self.required_permissions = set(permissions)

    async def check(self, obj: TelegramObject):
        if self.required_permissions is None:
            return True

        data = ctx_data.get()
        has_access = False
        for permission in self.required_permissions:
            has_access = has_access | bool(data.get(permission))

        return has_access


class RoleFilter(BoundFilter):
    key = 'role'

    def __init__(self, role: typing.Union[None, str, typing.Collection[str]] = None):
        if role is None:
            self.roles = None
        elif isinstance(role, str):
            self.roles = {role}
        else:
            self.roles = set(role)

    async def check(self, obj: TelegramObject):
        if self.roles is None:
            return True
        data = ctx_data.get()
        return data.get("role") in self.roles
