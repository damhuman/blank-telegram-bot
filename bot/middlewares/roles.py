from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from bot.utils.constants import USER, GUEST


class RoleMiddleware(LifetimeControllerMiddleware):
    # requires UserToContextMiddleware before
    skip_patterns = ["error", "update"]

    async def pre_process(self, obj, data, *args):
        if not hasattr(obj, "from_user") or obj.from_user is None:
            data["role"] = GUEST
            return

        user = data['user']
        if not user.role_id:
            data["role"] = GUEST
        else:
            # TODO CHANGE logic
            data["role"] = USER
            # role = db_con.get_role_by_id(user.role)
            # data["role"] = role.name

            # optionally add permission details
            # data[permission_type] = role.permission_type

    async def post_process(self, obj, data, *args):
        del data["role"]
