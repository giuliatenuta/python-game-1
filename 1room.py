filename="1room.txt"
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
		elif i=="m":
			i="[M]"
			print(i,end="")
		elif i==".":
			i="[ ]"
			print(i,end="")
		elif i=="#":
			i="[=]"
			print(i,end="")
		elif i=="/":
			i="(  "
			print(i,end="")
		elif i=="=":
			i="|  "
			print(i,end="")
		elif i=="*":
			i="  |"
			print(i,end="")
		elif i=="&":
			i="  )"
			print(i,end="")
		elif i=="p":
			i="[P]"
			print(i,end="")
		elif i=="b":
			i="[bi"
			print(i,end="")
		elif i=="c":
			i="ci]"
			print(i,end="")
		elif i=="+":
			i="[S]"
			print(i,end="")	
		else:
			print(i,end="")
file.close()
