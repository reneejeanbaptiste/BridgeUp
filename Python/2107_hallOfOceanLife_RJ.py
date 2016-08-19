import csv
import wikipedia as w
ocean_in = open ("CSVNewOceanLife2.csv", "rU") #opens file
scary_animals = list (csv.reader(ocean_in)) #allows file to be read
animal_topics = scary_animals [0] #prints out the first row?
animal_index = animal_topics.index  #makes you able to find a specific animal


#for row in scary_animals:
	#print row

def wiki_or_quit (decision,animal_name):
	if decision == "1":
		print w.summary(animal_name, "\n")
	elif decision == "2":
		print ("You're going back to the menu. ")
	else:
		print "Sorry, that's not an option."


def show_animal_data (animal_name):
	for i in scary_animals:
		if i[0]==animal_name: #if the 0 inde is equal to the string, then pritn all the data, etc. 
			print ("\n \n The " + i[0]+" lives in a " + i[2] + ", eats " + i[3] + ", is found in " + i[4] + ", is " + i[5] + " long, and its scientific name is "+i[6] + ". "+"An interesting fact about the "+i[0]+" is that it "+i[1]+".")
			wiki_or_quit(raw_input("\n \n If you would like to learn more about the "+ i[0]+", press 1. \n \n If you would like to quit the program, press 2:\n \n Your choice:	"), animal_name)


def menu ():
	print "Welcome to the menu! Pick an animal you would like to learn about. For each animal you can learn about a random fact, their habitat, diet, location, size, and scientific name. "
	user_choice = raw_input ("\n \n The options are The California Sheephead (1), the Decorator Crab (2), the Kelp Pipefish (3), and the Scorpion Fish (4). If you would like to quit, press 5. \n \n Which option do you choose?:  ")
	
	while user_choice != "5":
		if user_choice == "1":
			show_animal_data("California Sheephead")
		elif user_choice == "2":
			show_animal_data("Decorator Crab")
		elif user_choice == "3":
			show_animal_data("Kelp Pipefish")
		elif user_choice == "4":
			show_animal_data("Scorpionfish")
		else:
			print "Sorry, that's not an option."
			#user_choice = raw_input ("\n \n The options are The California Sheephead (1), the Decorator Crab (2), the Kelp Pipefish (3), and the Scorpion Fish (4). If you would like to quit, press 5. \n \n Which option do you choose?:  ")
		user_choice = raw_input ("\n \n The options are The California Sheephead (1), the Decorator Crab (2), the Kelp Pipefish (3), and the Scorpion Fish (4). If you would like to quit, press 5. \n \n Which option do you choose?:  ")
menu ()
    
    

    






