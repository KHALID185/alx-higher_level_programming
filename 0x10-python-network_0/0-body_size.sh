#!/bin/bash
# file to sends a request to URL and display the size of body
curl -sI "$1" | awk '/Content-Length/ {print $2}'
