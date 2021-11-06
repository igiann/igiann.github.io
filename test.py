#!/usr/bin/env python3
#import pandas as pd
import json
import requests
url='https://iptv-org.github.io/iptv/channels.json'

response = requests.get(url)
json_data = response.json()

def jsonfind(json_object, name):
    for dict in json_object:
        if dict['name'] == name:
            return dict

f = open("news.m3u", "w")

info = jsonfind(json_data,'France 24 English')
data = '#EXTM3U\n'

#punon
#for i in json_data:
#    if i['name']=='France':
#        print("Name:", i['url'])

#f = xbmcvfs.File('/path/to/file.m3u','w')

#for item in items:
data += '#EXTINF:-1 group-title="ΔΙΕΘΝΗ" tvg-name="%s" tvg-logo="%s",%s\n%s'% (info["tvg"]["id"],info["logo"],info["name"],info["url"])
f.write(data)
f.close() 
