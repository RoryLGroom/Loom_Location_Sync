#!/bin/bash

# exits if anything fails
set -e
# make sure everything is updated
sudo apt update
# whatever the top file of the 
PROJECT_DIR=home/rory/Desktop/Test
cd $PROJECT_DIR
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod +x script.sh

echo "Please import config file"
echo "Please set up crontab with 0 0,12 * * * /path/to/script.sh >> /path/to/cron.log 2>&1"

