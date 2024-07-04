#!/bin/bash
# file that send a post request type json and display the body of response
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
