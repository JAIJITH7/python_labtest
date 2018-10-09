import sys
args=sys.argv[1]
c=open("ip2.txt",'r')
with c as f:
	l=f.readlines()
	for x in l:
		x=x.split(' ')
		if args==x[0]:
			print("ip is present",args)
			break;
		else:
			print("ip not present")
	
sys.exit()

