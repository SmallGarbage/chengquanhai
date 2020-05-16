import json


def load_config():
    with open("../../../config/url.json") as f:
        config = json.load(f)
        return config


def load_time():
    with open("../../../config/time.json") as f:
        time = json.load(f)
        return time


def load_work_day():
    with open("../../../config/month_day.json") as f:
        month_day = json.load(f)
        return month_day
