import argparse
import base64
import json
import logging
import os
import pickle
import sys
from pathlib import Path
import requests
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta, date

currentDateAndTime = datetime.now()

load_dotenv(find_dotenv())
# setting up basic file structure
# parent is the current file's dir
BASE_DIR = Path(__file__).parent
DATA_DIR = os.path.join(BASE_DIR, os.environ.get("DATA_DIR"))
LOG_DIR = os.path.join(BASE_DIR, os.environ.get("LOG_DIR"))
OUTPUT_DIR = os.path.join(BASE_DIR, os.environ.get("OUTPUT_DIR"))
cached_data_path = os.path.join(BASE_DIR, "service.cache")

# setup command parser
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="Your username, overrides .env file.", required=False)
parser.add_argument("-p", "--password", help="Your password, overrides .env file.", required=False)
args = parser.parse_args()


def create_dir_if_it_does_not_exist(path):
    """
    Create a new directory if it does not exist
    """
    if not os.path.exists(path):
        os.makedirs(path)


create_dir_if_it_does_not_exist(DATA_DIR)
create_dir_if_it_does_not_exist(LOG_DIR)
create_dir_if_it_does_not_exist(OUTPUT_DIR)

# initialize python3 logger, is is a basic logger setup
logging.basicConfig(
    format='%(levelname)s: %(asctime)-15s: %(name)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=os.path.join(LOG_DIR, 'app_service.log'),
    level=logging.INFO
)
logger = logging.getLogger(__name__)
logger.error("Failed to save remaining ids to '%s' with error: %s", OUTPUT_DIR, "this is the error")
logger.info("Remaining IDs: {0}".format("this is a logger info"))

# setup username
if args.username:
    username = args.username
else:
    username = os.environ.get("USER")

# decode the encrypted password
if args.password:
    password = args.password
else:
    password = base64.b64decode(os.environ.get("TD_PASS")).strip().decode("utf-8")

global_val_to_save = {}


def load_previous_saved_data():
    global global_val_to_save
    if os.path.exists(cached_data_path):
        with open(cached_data_path, "rb") as fp:
            global_val_to_save.update(pickle.load(fp))
    logger.info("previous saved data is loaded")


def save_curr_result():
    global global_val_to_save
    with open(cached_data_path, "wb+") as output_file:
        pickle.dump(global_val_to_save, output_file)
    logger.info("cleaning information is saved")
