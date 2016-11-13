'''
Challenge 1 von pythonchallenge.com
Aufgabe: http://www.pythonchallenge.com/pc/def/map.htm
Loesung: http://www.pythonchallenge.com/pcc/def/ocr.html
Naechste: http://www.pythonchallenge.com/pc/def/ocr.html
'''

text_challenge = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

for i in range (0,len(text_challenge)):
	if ord(text_challenge[i]) < 97:
		print text_challenge[i],
	elif ord(text_challenge[i]) > 122:
		print text_challenge[i],
	elif ord(text_challenge[i]) == 121:
		print chr(97),
	elif ord(text_challenge[i]) == 122:
		print chr(98),
	else:
		letter_decrypt = chr(ord(text_challenge[i])+2)
		print letter_decrypt,