#!/usr/bin/python3
'''JSON Serialization'''
import json


def save_to_json_file(my_obj, filename):
    '''Write to JSON object'''
    with open(filename, 'w') as outfile:
        return json.dump(my_obj, outfile)
