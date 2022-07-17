# settings.py
import configparser
import logging
import os
from pathlib import Path


config = configparser.ConfigParser()
BASE_DIR = Path(__file__).parent
config.read(os.path.join(BASE_DIR, 'settings.ini'))
DATA_DIR = os.path.join(BASE_DIR, config.get('general', 'data_dir'))
LOG_DIR = os.path.join(BASE_DIR, config.get('general', 'log_dir'))
OUTPUT_DIR = os.path.join(BASE_DIR, config.get('general', 'output_dir'))
cached_data_path = os.path.join(BASE_DIR, config.get('general', 'app_cache_dir'))

# initialize python3 logger, is is a basic logger setup
logging.basicConfig(
    format='%(levelname)s: %(asctime)-15s: %(name)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=os.path.join(LOG_DIR, 'app_service.log'),
    level=logging.INFO
)

LDAP = dict(config.items('ldap'))
DPLY1_DATA = dict(config.items('dply1_data'))
CDAE1_DATA = dict(config.items('cdae1_data'))
NEXUS_PLATFORM = dict(config.items('nexus_platform'))
LOCAL_FILES = dict(config.items('local_file'))
