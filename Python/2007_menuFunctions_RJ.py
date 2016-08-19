  import 1807_DNA_RJ
def menu():
	choice =  raw_input(" Choose between composition which is choice A , transcribing which is choice B and choice C which is translate by typing your choice!!!").upper()
	if choice=="A":
		comp()
	elif choice=="B":
		transcribing()
	elif choice=="C":
		translate()
	else: 
		print("The variable you have typed is not A,B or C. Type A,B or C")
