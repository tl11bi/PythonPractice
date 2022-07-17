import os
import time
from datetime import datetime, date


def to_epoch_time(date_time: str) -> int:
    """
    converting string datetime to epoc time
    :param date_time: string datetime to epoc time
    :return:
    """
    os.environ['TZ'] = 'UTC'
    p = "%Y%m%d-%H%M%S"
    return int(time.mktime(time.strptime(date_time, p)))

