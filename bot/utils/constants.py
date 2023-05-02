from enum import Enum

GUEST = "Guest"
USER = "User"
ADMIN = "Admin"
SUPERADMIN = "SuperAdmin"

# permissions for read only in chat
RESTRICTED_PERMISSION_FOR_USER = {
    'can_send_messages': False,
    'can_send_media_messages': False,
    'can_send_polls': False,
    'can_send_other_messages': False,
    'can_add_web_page_previews': False,
    'can_change_info': False,
    'can_invite_users': False,
    'can_pin_messages': False
}

# default permissions for users in chat
DEFAULT_PERMISSION_FOR_USER = {
    'can_send_messages': True,
    'can_send_media_messages': True,
    'can_send_polls': True,
    'can_send_other_messages': True,
    'can_add_web_page_previews': True,
    'can_change_info': False,
    'can_invite_users': False,
    'can_pin_messages': False
}

ADMIN_PANEL_PAGE_SIZE = 20


class Language(Enum):
    ua = 'ua'
    en = 'en'


DEFAULT_LANGUAGE = Language.ua.value
