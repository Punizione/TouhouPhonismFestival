#!/bin/sh
location = "/root/TouhouPhonismFestival/App/temp"

find $location -mtime +1 -type f  -name *.mp3 -exec rm -f {}