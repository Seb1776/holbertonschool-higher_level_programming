#!/bin/bash
# Send a request and save the length
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
