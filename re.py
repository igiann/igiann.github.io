#!/usr/bin/env python3

import requests

def url_checker(url):
	try:
		#Get Url
		get = requests.get(url)
		# if the request succeeds
		if get.status_code == 200:
			print(" is reachable")
		else:
			print("asdfxxxxxxxxxxxxxxxxxxxxx")
	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		print("asdf")
x = "www.google.com"

url_checker(x)
