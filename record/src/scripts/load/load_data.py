import json
import requests
from load_config.load_file import load_config, load_time
from utils.time_convert import time_convert

config = load_config()
_time = load_time()


def get_token():
    url = config["url"]
    corpid = config["corpid"]
    corpsecret = config["corpsecret"]
    token_get_url = "{}/cgi-bin/gettoken?corpid={}&corpsecret={}".format(url, corpid, corpsecret)
    token = requests.get(token_get_url).json()["access_token"]
    return token


def load_data():
    start_time = time_convert(_time["start_time"])
    end_time = time_convert(_time["end_time"])
    url = config["url"]
    token = get_token()
    get_data_url = url + "/cgi-bin/corp/getapprovaldata?access_token={}".format(token)
    time = json.dumps({"starttime": start_time, "endtime": end_time})
    data = requests.post(get_data_url, data=time).json()["data"]
    return data


if __name__ == '__main__':
    data = load_data("2020-04-01 00:00:00", "2020-05-01 00:00:00")
    print(data)
