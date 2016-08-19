def menu():
	choice =  raw_input(" Choose between composition which is choice A , transcribing which is choice B and choice C which is translate by typing your choice!!! Type QUIT to quit").upper()

	while choice != "QUIT":
		if choice=="A":
			DNA = raw_input("Enter a new DNA strand").upper()  #getting strand from user
			print("blah" + str(comp(DNA)))  #need to print this out
		elif choice=="B":
			DNA = raw_input("Enter a new DNA strand").upper() #getting strand from user
			print("blah" + str(transcribing(DNA)))  #need to print this out
		elif choice=="C":
			DNA = raw_input("Enter a new DNA strand").upper() #getting strand from user
			print("blah" + str(translate(RNA)))  #need to print this out
		else: 
			print("The variable you have typed is not A,B or C. Type A,B or C")
		choice = raw_input("Choose A,B,C and QUIT")

def comp(DNA):
	strand_new=""
	for base in DNA:
		if base == "A":
			strand_new=strand_new+"T"
		elif base =="T":
			strand_new=strand_new+"A"
		elif base =="G":
			strand_new=strand_new+"C"
		elif base =="C":
			strand_new=strand_new+"G"
	return strand_new

def transcribing(DNA):
	strand_new=""
	for base in DNA:
		if base == "A":
			strand_new=strand_new+"U"
		elif base =="T":
			strand_new=strand_new+"A"
		elif base =="G":
			strand_new=strand_new+"C"
		elif base =="C":
			strand_new=strand_new+"G"
	return strand_new

def translate(RNA):
	strand_new=""
	for x in range(0,len(RNA),3):
		first=RNA[x]
		second=RNA[x+1]
		third=RNA[x+2]
		if first=="U":
			if second=="U":
				if third=="C" or third=="U":
					strand_new=strand_new+" Phe"
				else:
					strand_new=strand_new+" Leu"
			elif second=="C":
				strand_new=strand_new+" Ser"
			elif second=="A":
				if third=="U" or third =="C":
					strand_new=strand_new+" Tyr"
				elif third=="A" or third=="G":
					break
			elif second=="G":
				if third=="U" or third=="C":
					strand_new=strand_new+" Cys"
				elif third=="A":
					break
				elif third=="G":
					strand_new=strand_new+" Trp"
		elif first=="C":
			if second=="U":
					strand_new=strand_new+" Leu"				
			elif second=="C":
				strand_new=strand_new+" Pro"
			elif second=="A":
				if third=="U" or third =="C":
					strand_new=strand_new+" His"
				elif third=="A" or third=="G":
					strand_new=strand_new+" Gln"
			elif second=="G":
				strand_new=strand_new+" Arg"
		elif first=="A":
			if second=="U":
				if third=="C" or third=="U" or third=="A":
					strand_new=strand_new+" Ile"
				else:
					strand_new=strand_new+" Met"
			elif second=="C":
				strand_new=strand_new+" Thr"
			elif second=="A":
				if third=="U" or third =="C":
					strand_new=strand_new+" Asn"
				elif third=="A" or third=="G":
					strand_new=strand_new+" Lys"
			elif second=="G":
				if third=="U" or third=="C":
					strand_new=strand_new+" Ser"
				elif third=="A" or third=="G":
					strand_new=strand_new+" Arg"
		elif first=="G":
			if second=="U":
					strand_new=strand_new+" Val"
			elif second=="C":
				strand_new=strand_new+" Ala"
			elif second=="A":
				if third=="U" or third =="C":
					strand_new=strand_new+" Asp"
				elif third=="A" or third=="G":
					strand_new=strand_new+" Glu"
			elif second=="G":
					strand_new=strand_new+" Gly"
	return strand_new

# comp(DNA)
# print(comp(DNA))		
# print(transcribing(DNA))
# print(translate(transcribing(DNA)))

menu()
