#!/bin/bash
clear
echo -e "\033[1;31m[+] DEPLOYING RUENYAI CORE CORE FRAMEWORK ENVIRONMENT..."
sleep 1
mkdir -p utils modules
pip install -r requirements.txt
clear
python main.py
