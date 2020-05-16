import datetime
import time
import warnings


def time_convert(time_str):
    time_str = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    if time_str > datetime.datetime.now():
        warnings.warn("pls input rational parameter")
    else:
        time_str = datetime.datetime.strftime(time_str, "%Y-%m-%d %H:%M:%S")
        timeArray = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        return timeStamp


if __name__ == '__main__':
    time_convert("2019-12-20 23:40:00")
