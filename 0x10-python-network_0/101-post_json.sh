#!/bin/bash
# Send a request and save the length
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
