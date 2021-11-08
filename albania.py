	#!/usr/bin/env python

import requests

f = open("al.m3u", "r")
#
def testurl(url):
#    try:
#        response = requests.get(url)
#        print("OK")
#    except requests.ConnectionError as exception:
#        print("DOWN")
   response = requests.get(url)
   if response.status_code == 200:
       print("test")

for x in f:
    
    if x[0]=="#":
        continue
    testurl(x)
    print(x)
f.close()

