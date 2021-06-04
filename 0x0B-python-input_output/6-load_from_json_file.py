#!/usr/bin/python3
'''JSON Serialization'''
import json


def load_from_json_file(filename):
    '''
    Creates an object from a JSON File
    filename -- Name of the file
    '''
    with open(filename) as f:
        return json.load(f)
