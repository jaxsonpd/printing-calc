## @file configuration.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-06-06
#  @brief A custom configuration reader file to simplify reading json files
#
#  @cite https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file

import json
from typing import Union

class ConfigDict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class Config(object):
    @staticmethod
    def __load__(data):
        if type(data) is dict:
            return Config.load_dict(data)
        elif type(data) is list:
            return Config.load_list(data)
        else:
            return data

    @staticmethod
    def load_dict(data: dict):
        result = ConfigDict()
        for key, value in data.items():
            result[key] = Config.__load__(value)
        return result

    @staticmethod
    def load_list(data: list):
        result = [Config.__load__(item) for item in data]
        return result

    @staticmethod
    def load_json(path: str) -> Union[ConfigDict, list]:
        with open(path, "r") as f:
            result = Config.__load__(json.loads(f.read()))
        return result


