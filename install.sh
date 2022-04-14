#!/usr/bin/env bash

pip3 install -r requirements.txt
mkdir -p ~/.config/wayweather
cp ./wayweather.yml ~/.config/wayweather/wayweather.yml
mkdir ~/bin
cp ./wayweather.py ~/bin/wayweather.py
chmod +x ~/bin/wayweather.py
