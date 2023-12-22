#!/bin/bash

pkill -15 -f microdot_feed.py
rm /home/pi/microdot.flag

python3 /home/pi/microdot_reset.py
