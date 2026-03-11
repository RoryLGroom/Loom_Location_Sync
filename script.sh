#!/bin/bash

# outputs commands in the cron log
set -x
# locates directory where script.sh lives
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
# runs python script, and stores output in script_output.txt
$PROJECT_DIR/.venv/bin/python example.py >> $PROJECT_DIR/script_output.txt 2>&1
