#!/bin/bash
# Send a request and save the length
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
