'''
Challenge 6 von pythonchallenge.com
Aufgabe: http://www.pythonchallenge.com/pc/def/channel.html
Loesung: http://www.pythonchallenge.com/pcc/def/oxygen.html
Naechste: http://www.pythonchallenge.com/pc/def/oxygen.html
'''

import re, zipfile

archive = zipfile.ZipFile('06_challenge.zip', 'r')

nextid = '90052'
nextfile = nextid + ".txt"
myregex = r"nothing is (.+)"
comments = []

while re.findall(myregex, archive.read(nextfile)):
	myregexfind = re.findall(myregex, archive.read(nextfile))
	nextid = myregexfind[0]
	nextfile = nextid + ".txt"
	comments.append(archive.getinfo(nextfile).comment)

print("".join(comments))