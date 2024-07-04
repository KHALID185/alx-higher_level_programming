#!/bin/bash
# display all http method server accept
curl -si "$1" | awk -F ": " '/Allow/ {print $2}'
