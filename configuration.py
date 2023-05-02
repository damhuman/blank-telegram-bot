import configparser
import os

from dotenv import load_dotenv

load_dotenv()

# Bot configuration
TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')

# Database configuration
DB_URL = os.getenv('DB_URL')

# Utility configuration
USE_REDIS = os.getenv('USE_REDIS')
DATE_FORMAT = "%d.%m.%Y %H:%M UTC"
LOGGING_FILE_PATH = os.getenv('LOGGING_FILE_PATH', None)

# for custom nodes report
NODES_SUB_TYPE_ID = os.getenv('NODES_SUB_TYPE_ID')

# admin panel config
ADMIN_PANEL_SECRET_KEY = os.getenv('ADMIN_PANEL_SECRET_KEY')
ADMIN_PANEL_BASIC_AUTH_USERNAME = os.getenv('ADMIN_PANEL_BASIC_AUTH_USERNAME')
ADMIN_PANEL_NAME = os.getenv('ADMIN_PANEL_NAME')
ADMIN_PANEL_BASIC_AUTH_PASSWORD = os.getenv('ADMIN_PANEL_BASIC_AUTH_PASSWORD')


en_config = configparser.ConfigParser()
ua_config = configparser.ConfigParser()
# Load strings.ini files for each language
en_config.read('bot/locales/en/strings.ini')
ua_config.read('bot/locales/ua/strings.ini')

strings = {
    'en': en_config,
    'ua': ua_config
}
