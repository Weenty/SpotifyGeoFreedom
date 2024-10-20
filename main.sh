#!/bin/bash
apt install python3
# apt install python3-venv
# python3 -m venv venv
# source venv/bin/activate
pip install -r req.txt
python.exe ./main.py --login="$LOGIN" --password="$PASS"