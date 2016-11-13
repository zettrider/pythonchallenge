'''
Challenge 4 von pythonchallenge.com
Aufgabe: http://www.pythonchallenge.com/pc/def/linkedlist.php
Loesung: http://www.pythonchallenge.com/pcc/def/peak.html
Naechste: http://www.pythonchallenge.com/pc/def/peak.html
'''

import urllib2,re

'''def getnext():
	global staticurl, nextid, nexturl, myregex, myregexfind, html, response
		
	print(html)
	print(nextid)
	print(myregexfind)
	nextid = myregexfind
	print(nextid)
	nexturl = staticurl + nextid
'''

html = "next nothing is 12345"
staticurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='	
nextid = '8022'
nexturl = staticurl + nextid
myregex = r"next nothing is (.+)"


while re.findall(myregex, html):
	response = urllib2.urlopen(nexturl)
	html = response.read()
	myregexfind = re.findall(myregex, html)
	nextid = myregexfind[0]
	nexturl = staticurl + nextid
	print("Regex passt")
	print html
	print nextid
	print nexturl

else:
	print html