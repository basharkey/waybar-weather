#!/usr/bin/env python3
import pathlib
import yaml
import requests
from bs4 import BeautifulSoup
import re

config_paths = [
    '.config/wayweather.yml',
    '.config/wayweather.yaml',
    '.config/wayweather/wayweather.yml',
    '.config/wayweather/wayweather.yaml'
]

for path in config_paths:
    config_file = pathlib.Path(pathlib.Path.home(), path)
    if config_file.is_file():
       break

try:
    with open(config_file) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
except Exception as err:
     raise OSError("config not found") from err

try:
    output_len = config['output_length']
    location_id = config['location_id']
except Exception as err:
    raise KeyError("invalid config") from err

url = f'https://weather.gc.ca/forecast/hourly/on-{location_id}_metric_e.html'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
hours = soup.find_all('tr')

data = []
for hour in hours:
    try:
        time = hour.find('td', attrs={'headers':'header1'}).text.strip(' ')
        temp = hour.find('td', attrs={'headers':'header2'}).text.strip(' ')
        cond = hour.find('td', attrs={'headers':'header3'}).text.strip(' ')
        precip = hour.find('td', attrs={'headers':'header4'}).text.strip(' ')
        wind = hour.find('td', attrs={'headers':'header5'}).text.split(' ')
        wind_direction = wind[0]
        wind_speed = wind[1]
        data.append({'time': time, 'temp': temp, 'precip': precip, 'wind_direction': wind_direction, 'wind_speed': wind_speed})
    except:
        pass

print("|", end="")
for i in range(output_len):
    print(f" {data[i]['time']} {data[i]['temp']:>4}° {data[i]['precip']:>4}% {data[i]['wind_direction']:>3} {data[i]['wind_speed']:>3} km/h", end=" |")

