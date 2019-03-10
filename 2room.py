filename="2room.txt"
file=open(filename,"r")
c=file.readlines()
for a in c:
	for i in a:
		if i=="-":
			i="[#]"
			print(i,end="")
		elif i=="0":
			i=" __"
			print(i,end="")
		elif i=="s":
			i="[S]"
			print(i,end="")
		elif i==".":
			i="[ ]"
			print(i,end="")
		elif i=="/":
			i="(  "
			print(i,end="")
		elif i=="*":
			i="  )"
			print(i,end="")
		elif i=="p":
			i="[P]"
			print(i,end="")
		elif i=="%":
			i="[A]"
			print(i,end="")
		elif i=="q":
			i="[Q]"
			print(i,end="")	
		elif i=="1":
			i="| |"
			print(i,end="")
		else:
			print(i,end="")
file.close()
