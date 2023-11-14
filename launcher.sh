#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /home/pi/
source env/bin/activate
cd /home/pi/PythonTeams
python PushButtonSend.py
