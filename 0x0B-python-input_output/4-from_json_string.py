#!/usr/bin/python3
'''JSON Serialization'''
import json


def from_json_string(my_str):
    '''String serialization'''
    return json.loads(my_str)
