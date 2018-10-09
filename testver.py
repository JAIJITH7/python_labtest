import sys
args=sys.argv[1]
count=0
c=open("ipver.txt",'r')
with c as f:
	for line in f:
		if args in line:
			print("ip is present",args)
			count=count+1
		
print(count)
sys.exit()


	
