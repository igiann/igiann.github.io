#! /usr/bin/env python
# the content of test-requests.py
import requests
from requests import get
url='http://144.76.86.51:57060/stalker/zacj5NaQuQ7P3oPI/22'
#r = requests.get(url)
#if r.status_code==200:
#    print('OK') 
try:
    response = requests.get(url)
    print("OK")
except requests.ConnectionError as exception:
    print("DOWN")
