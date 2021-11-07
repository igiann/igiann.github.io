#!/usr/bin/env python3

import json
import requests

url='https://iptv-org.github.io/iptv/channels.json'

response = requests.get(url)
json_data = response.json()

# Function for finding the channel you want
def jsonfind(json_object, name):
    for dict in json_object:
        if dict['name'] == name:
            return dict

# Create the list file
listchannels=['Sky News','CNN International Europe','France 24 English','BBC News','Rai 1',
'Rai News 24','ABC News','Al Jazeera English','TV5 Monde Europe']
f = open("news.m3u", "w")
data = '#EXTM3U\n'
for channel in listchannels:
    info = jsonfind(json_data,channel)

    data += '#EXTINF:-1 group-title="International" tvg-name="%s" tvg-logo="%s",%s\n%s\n'% (info["tvg"]["id"],info["logo"],info["name"],info["url"])
f.write(data)
f.close() 
