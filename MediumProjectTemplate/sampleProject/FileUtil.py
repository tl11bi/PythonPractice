from datetime import datetime
from os import path


def insert_single_dir_into_file(self, data_to_insert: dir):
    date_time = load_json_file(_dat_time_file)
    date_time.append(data_to_insert)
    write_json_file(_dat_time_file, date_time)

def write_json_file_with_date_malcode(self, file_name: str, list_to_save: list):
    file_path = _file_save_path + '/' + _malcode + "_" + file_name + '_' + date_time_tag + '.json'
    __write_to_json_file(file_path, list_to_save)

def write_json_file(self, file_name: str, list_to_save: list):
    file_path = _file_save_path + '/' + file_name + '.json'
    __write_to_json_file(file_path, list_to_save)

def __write_to_json_file(self, file_path: str, list_to_save: list):
    with open(file_path, 'w') as f:
        json.dump(list_to_save, f)
    logger.info('File is created and saved to ' + file_path)

def load_json_file(self, file_name: str) -> list:
    file_path = _file_save_path + '/' + file_name + '.json'
    with open(file_path) as f:
        data = json.load(f)
    return data

def get_data_frame(self, file_name):
    file_path = _file_save_path + '/' + file_name + '.json'
    return pd.read_json(file_path, convert_dates=False)

@property
def date_time_tag(self) -> str:
    return _curr_time.strftime("%Y%m%d-%H%M%S")

@property
def date_tag(self) -> str:
    return _curr_time.strftime("%Y-%m-%d")

@property
def date_time_epoch(self) -> int:
    return int(_curr_time.timestamp())