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

f = open("news.m3u", "w")
info = jsonfind(json_data,'France 24 English')
data = '#EXTM3U\n'

data += '#EXTINF:-1 group-title="ΔΙΕΘΝΗ ΔΙΚΤΥΑ" tvg-name="%s" tvg-logo="%s",%s\n%s'% (info["tvg"]["id"],info["logo"],info["name"],info["url"])
f.write(data)
f.close() 
