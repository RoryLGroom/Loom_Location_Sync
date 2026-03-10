#!/bin/bash
set -x
cd /home/rory/Desktop/Loom_Map
source .venv/bin/activate
cd /home/rory/Desktop/Loom_Map/src
python3 example.py >> script_output.txt 2>&1
