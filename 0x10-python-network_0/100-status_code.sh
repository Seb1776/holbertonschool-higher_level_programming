#!/bin/bash
# Send a request and save the length
curl -o /dev/null -s -w "%{http_code}" "$1"
