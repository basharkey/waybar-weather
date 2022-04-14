#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

output_len = 3
location_id = "31fa7b6da0d67b704f144e94301d921023ab7bfe5a7de83b036bb1a652989d23"
url = "https://weather.com/en-IN/weather/hourbyhour/l/" + location_id

resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")
hours = soup.find_all("details", id=re.compile("detailIndex.*"))

data = []
for hour in hours:
    time = hour.find("h3", attrs={"data-testid":"daypartName"}).text
    temp = hour.find("span", attrs={"data-testid":"TemperatureValue"}).text
    precip = hour.find("span", attrs={"data-testid":"PercentageValue"}).text
    wind = hour.find("span", attrs={"data-testid":"Wind"}).text
    data.append([time, temp, precip, wind])

print("|", end="")
for i in range(output_len):
    print(" " + data[i][0], data[i][1], data[i][2], data[i][3], end=" |")
