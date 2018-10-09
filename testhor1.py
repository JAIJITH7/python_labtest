# File input text has a string of IP's. From the CLA, get the input and match the existance

import sys
userInput=sys.argv[1]

with open('iphor1.txt') as f:
	ipFile=f.readlines()
	for ip in ipFile:
		ipadd1, ipadd2 = ip.strip().split(" ",1)

matched=True
while matched:
	if userInput==ipadd1:
	   print(True)
	else: 
	   print(False)
	   
	matched=False
	break
		
