#!/bin/bash
# file will take a url as argument and traite get request
curl "$1" -sX GET -H "X-School-User-Id: 98"
