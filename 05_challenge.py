'''
Challenge 5 von pythonchallenge.com
Aufgabe: http://www.pythonchallenge.com/pc/def/peak.html
Loesung: http://www.pythonchallenge.com/pcc/def/channel.html
Naechste: http://www.pythonchallenge.com/pc/def/channel.html
'''

from urllib.request import urlopen
import pickle

h = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(h)

for line in data:
    print("".join([k * v for k, v in line]))
