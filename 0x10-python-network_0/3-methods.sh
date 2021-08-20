#!/bin/bash
# Send a request and save the length
curl -sI "$1" | grep Allow | cut -d' ' -f2-
