import random
import numpy as np
from tkinter import *
import winsound

ingameminutes = 0
ingameseconds = 0

count_of_wood = 0
c_of_wood = 4
c_of_stoneforaxe = 2

time_of_globe = str()
first = None
second = None
third = None
four = None
craftitem = None
standart = 19
class item:
	id = 0 # index
	name = str() 
	k = 0 #count
	x = 0 #X-coord
	z = 0 #Z-coord
	
	
	def p(self):			#
		print(self.name)    # p is func for Inventory part of code
		print(self.k)       #

GlStonex = None
GlStoney = None
wood = item()
wood.name = "wood"
wood.id = 1
	
sapling = item()
sapling.name = "sapling"
sapling.id = 2

class axe:
	x = 0
	z = 0
	aleb = False
	standart = False
	usage = None
	damage = 0
	manahave = 0
	id = 0
	name = str()
	level = 0
	
	def p(self):
		print(self.name)
		print("Usage: ", self.usage)
		print("level: ", self.level)

class player:
	health = 100
	hunger = 200
	mana = 10
	x = 0
	z = 0
	instrument = [axe()]
	inventories = [item(), item(), item(), item(), item()]

player1 = player()

class weaponbleed:
	x = 0
	z = 0
	damage = 0
	special1 = None
	special2 = None
	upgrade1 = False
	upgrade2 = False
	upgradechar = False
	char = None
	char2 = None
	id = 0
	name = str()
	usage = None

class weaponrange:
	x = 0
	z = 0
	throw = False
	bow = False
	gun = False
	damage = 0
	Vmagz = 0
	magz = 0
	magzhave = 0
	special1 = None
	special2 = None
	upgrade1 = False
	upgrade2 = False
	upgradechar = False
	char = None
	char2 = None
	id = 0
	name = str()
	usage = None

class weaponmagic:
	x = 0
	z = 0
	damage = 0
	manahave = 0
	book = False
	stick = False
	bigstick = False
	grimmuar = False
	dakaten = False
	bleed = False
	range = False
	special1 = None
	special2 = None
	upgrade1 = False
	upgrade2 = False
	upgradechar = False
	char = None
	char2 = None
	id = 0
	name = str()
	
class pickaxe:
	x = 0
	z = 0
	usage = None
	damage = 0
	manahave = 0
	id = 0
	name = str()
	level = 0

class Tree:
	posx = random.randint(1, 40)
	posz = random.randint(-40, 40)
	cutted = False
	stage = 0
b = [[random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
     [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)],
	 [random.randint(0, 40), random.randint(-39, 39)]]
	 
stones_mass = [[random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
		       [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
    		   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)],
			   [random.randint(0, 40), random.randint(-39, 39)]]

iron_mass =	 [[random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
		      [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
    		  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],
			  [random.randint(-40, -5), random.randint(-39, 39)],]
Mass_Globe = []

Tree1 = Tree()
question = str()
x = 0
z = 0
x_preposition = x - 1
z_preposition = z - 1

exit = False

Tree1.intreetimer = random.randint(1, 120)

if Tree1.intreetimer <= 30:
	Tree1.stage = 1
elif Tree1.intreetimer <= 60:
	Tree1.stage = 2
elif Tree1.intreetimer <= 90:
	Tree1.stage = 3 
elif Tree1.intreetimer <= 120:
	Tree1.stage = 4

def stonenaxe_process():
		question = input("You meet tree. Have you cut them? Y/N:")
		if question == "Y":
			print("cut")
			input()
			print("cut again")
			input()
			print("Hit!")
			input()
			print("Finish him!")
			input()
			Tree1.cutted = True	
def Woodenaxe_process():
		question = input("You meet tree. Have you cut them? Y/N:")
		if question == "Y":
			print("cut")
			input()
			print("cut again")
			input()
			print("Hit!")
			input()
			print("I think this wasn't great idea...")
			input()
			print("Finish him!")
			input()
			Tree1.cutted = True	
start_snd = True
if start_snd == True:
	print("You awaken in front of a broken structure of strange white material that emits a faint whitish light. You did not plan to get here, but there is no way back. You take a deep breath, because View is right here - a sky of a pleasant cyanoge color, filled with stars, against which you can see a huge number of planets that are close to each other. The closest thing to you is a huge planet, most likely the place where you are is its satellite.\n \nHaving gathered all the will into a fist, your head begins to think about what to do next in this situation.")
	winsound.PlaySound("True-Quark-Day.wav", 1)
	start = input("Press F to Start")
	start_snd = False
	pass
	
while not exit:
# input user module
	
	a = input()
	
	if a == "n":
		exit = True
	
	if player1.health <= 0:
		print("You are ded...")
		input()
		exit = True
#up
	if (player.x <= 41) and (a == "w"):
		player.x += 1
	
	if (player.x > 41) and (a == "w"):
		print("This location is inDEV")
		player.x -= 1	

#down	
	
	if (player.x > 0) and (player.x <= 41) and (a == "s"):
		player.x -= 1
	
	if (player.x < -41) and (a == "s"):
		print("This location is inDEV")
		player.x += 1

	if (player.x <= 0) and (player.x >= -41) and (a == "s") and ((player1.instrument[0].name == "") or (player1.instrument[0].name == None)):
		if (player.x <= 0) and (player.x >= -41) and (a == "s") and ((player1.instrument[0].name == "wooden pickaxe"):
			if (player.x <= 0) and (player.x >= -41) and (a == "s") and ((player1.instrument[0].name == "stone pickaxe"):
				print("Stone wall are here you kicked it...")
				input()
				print("Kicked again.")
				input()
				print("Tuk-Tuk")
				input()
				print("I think this wasn't great idea...")
				input()
				print("Kick")
				input()
				print("Smash")
				input()
				print("Sweaty.")
				input()
				print("You is monster, that can crash it wall, lol)")
				input()
				print("Finish it!")
				input()
				print("Ha!")
				input()
				print("Finish!")
				input()
				player.x -= 1
				player1.instrument[0].usage -= random.randint(1, 4)	
			print("Stone wall are here you kicked it...")
			input()
			print("Kicked again.")
			input()
			print("And again.")
			input()
			print("Tuk-Tuk")
			input()
			print("I think this wasn't great idea...")
			input()
			print("Kick")
			input()
			print("Smash")
			input()
			print("Sweaty.")
			input()
			print("You is monster, that can crash it wall, lol)")
			input()
			print("Finish it!")
			input()
			print("Ha!")
			input()
			print("Finish!")
			input()
			player.x -= 1
			player1.instrument[0].usage -= random.randint(1, 5)	
		print("Stone wall are here you kicked it...")
		input()
		print("Kicked again.")
		input()
		print("And again.")
		player1.health += random.randint(-3, 0)
		input()
		print("Your arm is bloody, but you have to kick again.")
		player1.health += random.randint(-3, 0)
		input()
		print("I think this wasn't great idea...")
		input()
		print("Kick")
		input()
		print("Uf.........")
		player1.health += random.randint(-3, 0)
		input()
		print("SHIT!")
		player1.health += random.randint(-7, -3)
		input()
		print("You is monster, that can crash it wall, lol)")
		input()
		print("Finish it!")
		input()
		print("Ha!")
		player1.health += random.randint(-7, -3)
		input()
		print("Finish!")
		input()
		player.x -= 1
		
	
	if (player.x < -41) and (a == "s"):
		print("This location is inDEV")
		player.x = player.x + 1

#left	
	
	if (player.z <= 0) and (player.z >= -41) and a == "a" or player.z >= 0 and player.z <= 40 and a == "a":
		player.z = player.z - 1
		if player.z == -41:
			player.z = player.z + 1
	
	if player.x < 0 and player.x >= -20 and a == "a":
		print("dig")
		input()
		print("dig again")
		input()
		print("final")
		input()
		player.z = player.z - 1
#right
	
	if player.z >= 0 and player.z <= 40 and a == "d" or player.z <= 0 and player.z >= -40 and a == "d":
		player.z = player.z + 1
		if player.z == 41:
			player.z = player.z - 1
	
	if player.x < 0 and player.x >= -20 and a == "d":
		print("dig")
		input()
		print("dig again")
		input()
		print("final")
		input()
		player.z = player.z + 1
		
	u = [player1.x, player1.z]

#checkuserposition	
	
	if a == "t":
		print( " Your Position on x: " + str(player1.x)  + ";" + " Your Position on z: " + str(player1.z) )

#GlobalItemMarkers:
	if stones_mass == []:
		stones_mass = [[random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
				       [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)],
					   [random.randint(0, 40), random.randint(-39, 39)]]
#timer	
	
	ingameseconds = ingameseconds + 1
	if ingameseconds >= 60:
		ingameminutes = ingameminutes + 1
		ingameseconds = 0
	if ingameminutes >= 60:
		ingameminutes = 0
	
	if ingameminutes <= 10:
		time_of_globe = "rise"
	if ingameminutes > 10 and ingameminutes <= 20:
		time_of_globe = "day"
	if ingameminutes > 20 and ingameminutes <= 40:
		time_of_globe = "dawn"
	if ingameminutes > 40 and ingameminutes <= 60:
		time_of_globe = "night"
	
	if a == "e":
		print(str(ingameminutes) + " : " + str(ingameseconds))
	if a == "q":
		print(time_of_globe)

#treesmechanics			
	Tree1.intreetimer = Tree1.intreetimer + 1
	if Tree1.intreetimer > 120:
		Tree1.intreetimer = 120
	if Tree1.intreetimer <= 30:
		Tree1.stage = 1
	elif Tree1.intreetimer <= 60:
		Tree1.stage = 2
	elif Tree1.intreetimer <= 90:
		Tree1.stage = 3 
	elif Tree1.intreetimer <= 120:
		Tree1.stage = 4
	
	if Tree1.stage == 4:
		wood.k = 8
		sapling.k = 2
	
	elif Tree1.stage == 3:
		wood.k = 6
		sapling.k = 1
	
	elif Tree1.stage == 2:
		wood.k = 4
		sapling.k = 0	
	
	elif Tree1.stage == 1:
		wood.k = 2
		sapling.k = 0
	
	for e in Mass_Globe:
		if (u[0] == e[0]) and (u[1] == e[1]):
			question = input("On floor you see any items. Have you take it?Y/N")
			while question != "Y" and question != "N":
				question = input("On floor you see any items. Have you take it?Y/N")		
			if (question == "Y") and (e[e[4]] == wood.id):
				if (player1.inventories[0].k == 0):			
					player1.inventories[0].k = wood.k
					player1.inventories[0].name = wood.name
					
				elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
					player1.inventories[1].k = wood.k
					player1.inventories[1].name = wood.name
							
				elif (player1.inventories[1].k != 0) and ((player1.inventories[2].k == 0)):
					player1.inventories[2].k = wood.k
					player1.inventories[2].name = wood.name

				elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
					player1.inventories[3].k = wood.k
					player1.inventories[3].name = wood.name							
					
				elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
					player1.inventories[4].k = wood.k
					player1.inventories[4].name = wood.name	
						
				if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
					question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
					if question == "1":
						player1.inventories[0].k = 0
						player1.inventories[0].name = None
					if question == "2":
						player1.inventories[1].k = 0
						player1.inventories[1].name = None
					if question == "3":
						player1.inventories[2].k = 0
						player1.inventories[2].name = None						
					if question == "4":
						player1.inventories[3].k = 0
						player1.inventories[3].name = None
					if question == "5":
						player1.inventories[4].k = 0
						player1.inventories[4].name = None			
					if question == "N":
						print("Okay, i put it here.")
						Glwoodposx = player1.x
						Glwoodposz = player1.y
						wood.x = Glwoodposx
						wood.y = Glwoodposz
						vr_mass = []
						vr_mass.append(Glwoodposx)
						vr_mass.append(Glwoodposz)
						vr_mass.append(wood.id)
						Mass_Globe.append(vr_mass)
							
	for e in b:						
		if (Tree1.cutted == False) and (u[0] == e[0]) and (u[1] == e[1]) and (player1.instrument[0].name == "stone axe"):
			question = input("You meet tree. Have you cut them? Y/N:")
			if question == "Y":
				stonenaxe_process()
				Tree1.cutted = True
				player1.instrument[0].usage -= 1	
		
		elif (Tree1.cutted == False) and (u[0] == e[0]) and (u[1] == e[1]) and (player1.instrument[0].name == "wooden axe") :
			question = input("You meet tree. Have you cut them? Y/N:")
			if question == "Y":
				Woodenaxe_process()
				Tree1.cutted = True
				player1.instrument[0].usage -= 1
		
		elif (Tree1.cutted == False) and (u[0] == e[0]) and (u[1] == e[1]) and (player1.instrument[0].name == "" or player1.instrument[0].name == None ):
			question = input("You meet tree. Have you cut them? Y/N:")
			if question == "Y":
				print("cut")
				input()
				print("cut again")
				input()
				print("Au!")
				input()
				print("Hit!")
				input()
				print("I think this wasn't great idea...")
				input()
				print("Finish him!")
				input()
				Tree1.cutted = True
				
		if Tree1.cutted == True and (u[0] == e[0]) and (u[1] == e[1]):
			question = input("On floor you see any items. Have you take it?Y/N")
			while question != "Y" and question != "N":
				question = input("On floor you see any items. Have you take it?Y/N")			
			if question == "Y":
				if Tree1.stage == 4:
					if (player1.inventories[0].k == 0):			
						player1.inventories[0].k = wood.k
						player1.inventories[0].name = wood.name
					
					elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = wood.k
						player1.inventories[1].name = wood.name
							
					elif (player1.inventories[1].k != 0) and ((player1.inventories[2].k == 0)):

						player1.inventories[2].k = wood.k
						player1.inventories[2].name = wood.name

					elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = wood.k
						player1.inventories[3].name = wood.name							
					
					elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = wood.k
						player1.inventories[4].name = wood.name	
						
					if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
						question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
						if question == "1":
							player1.inventories[0].k = 0
							player1.inventories[0].name = None
						if question == "2":
							player1.inventories[1].k = 0
							player1.inventories[1].name = None
						if question == "3":
							player1.inventories[2].k = 0
							player1.inventories[2].name = None						
						if question == "4":
							player1.inventories[3].k = 0
							player1.inventories[3].name = None
						if question == "5":
							player1.inventories[4].k = 0
							player1.inventories[4].name = None			
						if question == "N":
							print("Okay, i put it here.")
							Glwoodposx = player1.x
							Glwoodposz = player1.y
							wood.x = Glwoodposx
							wood.y = Glwoodposz
							vr_mass = []
							vr_mass.append(Glwoodposx)
							vr_mass.append(Glwoodposz)
							vr_mass.append(wood.id)
							Mass_Globe.append(vr_mass)

					if (player1.inventories[0].k == 0):
						player1.inventories[0].k = sapling.k
						player1.inventories[0].name = sapling.name
					
					elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = sapling.k
						player1.inventories[1].name = sapling.name

					elif (player1.inventories[1].k != 0) and (player1.inventories[2].k == 0):
						player1.inventories[2].k = sapling.k
						player1.inventories[2].name = sapling.name
							
					elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = sapling.k
						player1.inventories[3].name = sapling.name
					
					elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = sapling.k
						player1.inventories[4].name = sapling.name	
					
					if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
						question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
						if question == "1":
							player1.inventories[0].k = 0
							player1.inventories[0].name = None
						if question == "2":
							player1.inventories[1].k = 0
							player1.inventories[1].name = None
						if question == "3":
							player1.inventories[2].k = 0
							player1.inventories[2].name = None
						if question == "4":
							player1.inventories[3].k = 0
							player1.inventories[3].name = None	
						if question == "5":
							player1.inventories[4].k = 0
							player1.inventories[4].name = None	
						if question == "N":
							print("Okay, i put it here.")
							Glsaplposx = player1.x
							Glsaplposz = player1.y
							sapling.x = Glsaplposx
							sapling.y = Glsaplposz
							sap_mass = []
							sap_mass.append(Glsaplposx)
							sap_mass.append(Glsaplposz)
							sap_mass.append(sapling.id)
							Mass_Globe.append(sap_mass)
							
				if Tree1.stage == 3:
					if (player1.inventories[0].k == 0):			
						player1.inventories[0].k = wood.k
						player1.inventories[0].name = wood.name
					
					elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = wood.k
						player1.inventories[1].name = wood.name
							
					elif (player1.inventories[1].k != 0) and ((player1.inventories[2].k == 0)):

						player1.inventories[2].k = wood.k
						player1.inventories[2].name = wood.name

					elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = wood.k
						player1.inventories[3].name = wood.name							
					
					elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = wood.k
						player1.inventories[4].name = wood.name	
						
					if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
						question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
						if question == "1":
							player1.inventories[0].k = 0
							player1.inventories[0].name = None
						if question == "2":
							player1.inventories[1].k = 0
							player1.inventories[1].name = None
						if question == "3":
							player1.inventories[2].k = 0
							player1.inventories[2].name = None						
						if question == "4":
							player1.inventories[3].k = 0
							player1.inventories[3].name = None
						if question == "5":
							player1.inventories[4].k = 0
							player1.inventories[4].name = None			
						if question == "N":
							print("Okay, i put it here.")
							Glwoodposx = player1.x
							Glwoodposz = player1.y
							wood.x = Glwoodposx
							wood.y = Glwoodposz
							vr_mass = []
							vr_mass.append(Glwoodposx)
							vr_mass.append(Glwoodposz)
							vr_mass.append(wood.id)
							Mass_Globe.append(vr_mass)

					if (player1.inventories[0].k == 0):
						player1.inventories[0].k = sapling.k
						player1.inventories[0].name = sapling.name
					
					elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = sapling.k
						player1.inventories[1].name = sapling.name

					elif (player1.inventories[1].k != 0) and (player1.inventories[2].k == 0):
						player1.inventories[2].k = sapling.k
						player1.inventories[2].name = sapling.name
							
					elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = sapling.k
						player1.inventories[3].name = sapling.name
					
					elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = sapling.k
						player1.inventories[4].name = sapling.name	
					
					if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
						question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
						if question == "1":
							player1.inventories[0].k = 0
							player1.inventories[0].name = None
						if question == "2":
							player1.inventories[1].k = 0
							player1.inventories[1].name = None
						if question == "3":
							player1.inventories[2].k = 0
							player1.inventories[2].name = None
						if question == "4":
							player1.inventories[3].k = 0
							player1.inventories[3].name = None	
						if question == "5":
							player1.inventories[4].k = 0
							player1.inventories[4].name = None	
						if question == "N":
							print("Okay, i put it here.")
							Glsaplposx = player1.x
							Glsaplposz = player1.y
							sapling.x = Glsaplposx
							sapling.y = Glsaplposz
							sap_mass = []
							sap_mass.append(Glsaplposx)
							sap_mass.append(Glsaplposz)
							sap_mass.append(sapling.id)
							Mass_Globe.append(sap_mass)
				
				if Tree1.stage == 2:
					if (player1.inventories[0].k == 0):			
						player1.inventories[0].k = wood.k
						player1.inventories[0].name = wood.name
					
					elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = wood.k
						player1.inventories[1].name = wood.name
							
					elif (player1.inventories[1].k != 0) and ((player1.inventories[2].k == 0)):

						player1.inventories[2].k = wood.k
						player1.inventories[2].name = wood.name

					elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = wood.k
						player1.inventories[3].name = wood.name							
					
					elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = wood.k
						player1.inventories[4].name = wood.name	
						
					if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
						question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
						if question == "1":
							player1.inventories[0].k = 0
							player1.inventories[0].name = None
						if question == "2":
							player1.inventories[1].k = 0
							player1.inventories[1].name = None
						if question == "3":
							player1.inventories[2].k = 0
							player1.inventories[2].name = None						
						if question == "4":
							player1.inventories[3].k = 0
							player1.inventories[3].name = None
						if question == "5":
							player1.inventories[4].k = 0
							player1.inventories[4].name = None			
						if question == "N":
							print("Okay, i put it here.")
							Glwoodposx = player1.x
							Glwoodposz = player1.y
							wood.x = Glwoodposx
							wood.y = Glwoodposz
							vr_mass = []
							vr_mass.append(Glwoodposx)
							vr_mass.append(Glwoodposz)
							vr_mass.append(wood.id)
							Mass_Globe.append(vr_mass)

					if (player1.inventories[0].k == 0):
						player1.inventories[0].k = sapling.k
						player1.inventories[0].name = sapling.name
					
					elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = sapling.k
						player1.inventories[1].name = sapling.name

					elif (player1.inventories[1].k != 0) and (player1.inventories[2].k == 0):
						player1.inventories[2].k = sapling.k
						player1.inventories[2].name = sapling.name
							
					elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = sapling.k
						player1.inventories[3].name = sapling.name
					
					elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = sapling.k
						player1.inventories[4].name = sapling.name	
					
					if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
						question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
						if question == "1":
							player1.inventories[0].k = 0
							player1.inventories[0].name = None
						if question == "2":
							player1.inventories[1].k = 0
							player1.inventories[1].name = None
						if question == "3":
							player1.inventories[2].k = 0
							player1.inventories[2].name = None
						if question == "4":
							player1.inventories[3].k = 0
							player1.inventories[3].name = None	
						if question == "5":
							player1.inventories[4].k = 0
							player1.inventories[4].name = None	
						if question == "N":
							print("Okay, i put it here.")
							Glsaplposx = player1.x
							Glsaplposz = player1.y
							sapling.x = Glsaplposx
							sapling.y = Glsaplposz
							sap_mass = []
							sap_mass.append(Glsaplposx)
							sap_mass.append(Glsaplposz)
							sap_mass.append(sapling.id)
							Mass_Globe.append(sap_mass)
				
				if Tree1.stage == 1:
					if (player1.inventories[0].k == 0):			
						player1.inventories[0].k = wood.k
						player1.inventories[0].name = wood.name
					
					elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = wood.k
						player1.inventories[1].name = wood.name
							
					elif (player1.inventories[1].k != 0) and ((player1.inventories[2].k == 0)):

						player1.inventories[2].k = wood.k
						player1.inventories[2].name = wood.name

					elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = wood.k
						player1.inventories[3].name = wood.name							
					
					elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = wood.k
						player1.inventories[4].name = wood.name	
						
					if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
						question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
						if question == "1":
							player1.inventories[0].k = 0
							player1.inventories[0].name = None
						if question == "2":
							player1.inventories[1].k = 0
							player1.inventories[1].name = None
						if question == "3":
							player1.inventories[2].k = 0
							player1.inventories[2].name = None						
						if question == "4":
							player1.inventories[3].k = 0
							player1.inventories[3].name = None
						if question == "5":
							player1.inventories[4].k = 0
							player1.inventories[4].name = None			
						if question == "N":
							print("Okay, i put it here.")
							Glwoodposx = player1.x
							Glwoodposz = player1.y
							wood.x = Glwoodposx
							wood.y = Glwoodposz
							vr_mass = []
							vr_mass.append(Glwoodposx)
							vr_mass.append(Glwoodposz)
							vr_mass.append(wood.id)
							Mass_Globe.append(vr_mass)

					if (player1.inventories[0].k == 0):
						player1.inventories[0].k = sapling.k
						player1.inventories[0].name = sapling.name
					
					elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = sapling.k
						player1.inventories[1].name = sapling.name

					elif (player1.inventories[1].k != 0) and (player1.inventories[2].k == 0):
						player1.inventories[2].k = sapling.k
						player1.inventories[2].name = sapling.name
							
					elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = sapling.k
						player1.inventories[3].name = sapling.name
					
					elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = sapling.k
						player1.inventories[4].name = sapling.name	
					
					if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
						question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
						if question == "1":
							player1.inventories[0].k = 0
							player1.inventories[0].name = None
						if question == "2":
							player1.inventories[1].k = 0
							player1.inventories[1].name = None
						if question == "3":
							player1.inventories[2].k = 0
							player1.inventories[2].name = None
						if question == "4":
							player1.inventories[3].k = 0
							player1.inventories[3].name = None	
						if question == "5":
							player1.inventories[4].k = 0
							player1.inventories[4].name = None	
						if question == "N":
							print("Okay, i put it here.")
							Glsaplposx = player1.x
							Glsaplposz = player1.y
							sapling.x = Glsaplposx
							sapling.y = Glsaplposz
							sap_mass = []
							sap_mass.append(Glsaplposx)
							sap_mass.append(Glsaplposz)
							sap_mass.append(sapling.id)
							Mass_Globe.append(sap_mass)
				
			elif question == "N":
				print("Let's search another place to hang out...")
				Tree1.cutted = False

		if Tree1.cutted == True:
			Tree1.cutted = False
			g_t_r = 0
			simp = len(b)
			print(simp)
			b.remove(b[random.randrange(g_t_r, simp)])
			simp = 0
			player1.x -= 1			
			
	if a == "b":
		print("Trees:")
		print(b)
		print("")
		print("Stones:")
		print(stones_mass)
		print("")
		print("Iron:")
		print(iron_mass)
#inventory organaiser
	
	if a == "i":
		n = 0
		print("##################---INVENTORY---##################")
		print("HEALTH: " + str(player1.health))
		print("HUNGER: " + str(player1.hunger))
		print("")
		pi = []
		just = len(player1.inventories)
		tim = 0
		while tim <= just:
			pi.append(range(just))
			tim += 1
		tim = 0
		for i in range(tim, just):
			n += 1
			print("SLOT " + str(n) + ":")
			player1.inventories[i].p()
		print("")
		print("Weapon:")
		player1.instrument[0].p()
		print("##################---INVENTORY---##################")
#stones
	
	for e in stones_mass:		
		if (u[0] == e[0]) and (u[1] == e[1]) and (player1.instrument[0].name == ""):						
			stone_ex = True
			stone = item()
			stone.id = 4
			stone.name = "stone"
			stone.k = random.randint(1,8)
			question = input("You found Stone. Have you take it?Y/N")
			while question != "Y" and question != "N":
				question = input("On floor you see any items. Have you take it?Y/N")			
			if question == "Y":
				if (player1.inventories[0].k == 0):			
						player1.inventories[0].k = stone.k
						player1.inventories[0].name = stone.name
					
				elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = stone.k
						player1.inventories[1].name = stone.name
							
				elif (player1.inventories[1].k != 0) and ((player1.inventories[2].k == 0)):

						player1.inventories[2].k = stone.k
						player1.inventories[2].name = stone.name

				elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = stone.k
						player1.inventories[3].name = stone.name							
					
				elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = stone.k
						player1.inventories[4].name = stone.name	
						
				if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
					question = input("You Inventory is full! What you have to drop?(print 1-5 or N)")
					if question == "1":
						player1.inventories[0].k = 0
						player1.inventories[0].name = None
					if question == "2":
						player1.inventories[1].k = 0
						player1.inventories[1].name = None
					if question == "3":
						player1.inventories[2].k = 0
						player1.inventories[2].name = None						
					if question == "4":
						player1.inventories[3].k = 0
						player1.inventories[3].name = None
					if question == "5":
						player1.inventories[4].k = 0
						player1.inventories[4].name = None			
					if question == "N":
						print("Okay, i put it here.")
						Glstoneposx = player1.x
						Glstoneposy = player1.y
						stone.x = Glstoneposx
						stone.y = Glstoneposy					
				stone_ex = False
			if stone_ex == False:
				g_t_r = 0
				simp = len(stones_mass)
				stones_mass.remove(stones_mass[random.randrange(g_t_r, simp)])
				simp = 0
				stone_ex = True
				player1.x -= 1		
		if question == "N":
			a = None
					
#craft system and recipes

#wooden axe	
	
	if a == "cr":
		craftitem = input("Name of crafted item:")
		if craftitem == "woodenaxe" or craftitem == "Woodenaxe":
			count_of_wood = 0
			first = input("Select first slot or skiping print Y/N:")
			second = input("Select second slot or skiping print Y/N:")
			third = input("Select third slot or skiping print Y/N:")
			four = input("Select four slot for skiping print Y/N:")
			megacont = [first, second, third, four]
			if all(megacont) == "N":
				a = input()
			for i in range(0, 3):
				#print(player1.inventories[i].name)
				if megacont[i] == "Y" and player1.inventories[i].name == "wood":
					count_of_wood += player1.inventories[i].k 
			print(count_of_wood)
			c_of_wood = 4
			if count_of_wood >= 4:
				for i in range(3, -1, -1):
					print("i=",i," ",player1.inventories[i].k," ",player1.inventories[i].name," ",count_of_wood, " ", c_of_wood)
					if megacont[i] == "Y" and player1.inventories[i].name == "wood":
						if player1.inventories[i].k <= c_of_wood:
							c_of_wood -= player1.inventories[i].k
							player1.inventories[i].k = 0
							if c_of_wood == 0:
								break
						else:
							player1.inventories[i].k -= c_of_wood
							c_of_wood = 0
							break
			woodenaxe = axe()
			woodenaxe.standart = True
			woodenaxe.usage = 10
			woodenaxe.id = 3
			woodenaxe.name = "wooden axe"
			player1.instrument[0].usage = 10
			player1.instrument[0].name = "wooden axe"
		
		if craftitem == "stoneaxe" or craftitem == "Stoneaxe":
			count_of_wood = 0
			count_of_stone = 0
			first = input("Select first slot or skiping print Y/N:")
			second = input("Select second slot or skiping print Y/N:")
			third = input("Select third slot or skiping print Y/N:")
			four = input("Select four slot for skiping print Y/N:")
			megacont = [first, second, third, four]
			if all(megacont) == "N":
				a = input()
			for i in range(0, 3):
				if megacont[i] == "Y" and player1.inventories[i].name == "wood":
					count_of_wood += player1.inventories[i].k 
				if megacont[i] == "Y" and player1.inventories[i].name == "stone":
					count_of_stone += player1.inventories[i].k 
				print(count_of_wood)
				print(count_of_stone)
			c_of_wood = 2
			c_of_stoneforaxe = 4
			if (count_of_wood >= 2) and (count_of_stone >= 4):
				for i in range(3, -1, -1):
					
					print("i=",i," ",player1.inventories[i].k," ",player1.inventories[i].name," ",count_of_wood, " ", c_of_wood)
					if megacont[i] == "Y" and player1.inventories[i].name == "wood":
						if player1.inventories[i].k <= c_of_wood:
							c_of_wood -= player1.inventories[i].k
							player1.inventories[i].k = 0
							if c_of_wood == 0:
								break
					
					print("i=",i," ",player1.inventories[i].k," ",player1.inventories[i].name," ",count_of_stone, " ", c_of_stoneforaxe)
					
					if megacont[i] == "Y" and player1.inventories[i].name == "stone":
						if player1.inventories[i].k <= c_of_stoneforaxe:
							c_of_stoneforaxe  -= player1.inventories[i].k
							player1.inventories[i].k = 0
							if c_of_stoneforaxe == 0:
								break
						else:
							player1.inventories[i].k -= c_of_stoneforaxe 
							c_of_stoneforaxe  = 0
							break
			stoneaxe = axe()
			stoneaxe.standart = True
			stoneaxe.usage = 20
			stoneaxe.id = 5
			stoneaxe.name = "stone axe"
			player1.instrument[0].usage = 20
			player1.instrument[0].name = "stone axe"
		
		elif craftitem == "woodenpickaxe" or craftitem == "Woodenpickaxe":
			count_of_wood = 0
			first = input("Select first slot or skiping print Y/N:")
			second = input("Select second slot or skiping print Y/N:")
			third = input("Select third slot or skiping print Y/N:")
			four = input("Select four slot for skiping print Y/N:")
			megacont = [first, second, third, four]
			if all(megacont) == "N":
				a = input()
			for i in range(0, 3):
				#print(player1.inventories[i].name)
				if megacont[i] == "Y" and player1.inventories[i].name == "wood":
					count_of_wood += player1.inventories[i].k 
			print(count_of_wood)
			c_of_wood = 4
			if count_of_wood >= 4:
				for i in range(3, -1, -1):
					print("i=",i," ",player1.inventories[i].k," ",player1.inventories[i].name," ",count_of_wood, " ", c_of_wood)
					if megacont[i] == "Y" and player1.inventories[i].name == "wood":
						if player1.inventories[i].k <= c_of_wood:
							c_of_wood -= player1.inventories[i].k
							player1.inventories[i].k = 0
							if c_of_wood == 0:
								break
						else:
							player1.inventories[i].k -= c_of_wood
							c_of_wood = 0
							break
			woodenpickaxe = pickaxe()
			woodenpickaxe.usage = 15
			woodenpickaxe.id = 6
			woodenpickaxe.name = "wooden pickaxe"
			player1.instrument[0].usage = 15
			player1.instrument[0].name = "wooden pickaxe"
		
		elif craftitem == "stonepickaxe" or craftitem == "Stonepickaxe":
			count_of_wood = 0
			count_of_stone = 0
			first = input("Select first slot or skiping print Y/N:")
			second = input("Select second slot or skiping print Y/N:")
			third = input("Select third slot or skiping print Y/N:")
			four = input("Select four slot for skiping print Y/N:")
			megacont = [first, second, third, four]
			if all(megacont) == "N":
				a = input()
			for i in range(0, 3):
				if megacont[i] == "Y" and player1.inventories[i].name == "wood":
					count_of_wood += player1.inventories[i].k 
				if megacont[i] == "Y" and player1.inventories[i].name == "stone":
					count_of_stone += player1.inventories[i].k 
				print(count_of_wood)
				print(count_of_stone)
			c_of_wood = 2
			c_of_stoneforaxe = 2
			if (count_of_wood >= 2) and (count_of_stone >= 2):
				for i in range(3, -1, -1):
					
					print("i=",i," ",player1.inventories[i].k," ",player1.inventories[i].name," ",count_of_wood, " ", c_of_wood)
					if megacont[i] == "Y" and player1.inventories[i].name == "wood":
						if player1.inventories[i].k <= c_of_wood:
							c_of_wood -= player1.inventories[i].k
							player1.inventories[i].k = 0
							if c_of_wood == 0:
								break
					
					print("i=",i," ",player1.inventories[i].k," ",player1.inventories[i].name," ",count_of_stone, " ", c_of_stoneforaxe)
					
					if megacont[i] == "Y" and player1.inventories[i].name == "stone":
						if player1.inventories[i].k <= c_of_stoneforaxe:
							c_of_stoneforaxe  -= player1.inventories[i].k
							player1.inventories[i].k = 0
							if c_of_stoneforaxe == 0:
								break
						else:
							player1.inventories[i].k -= c_of_stoneforaxe 
							c_of_stoneforaxe  = 0
							break
			stonepickaxe = pickaxe()
			stonepickaxe.usage = 25
			stonepickaxe.id = 7
			stonepickaxe.name = "stone pickaxe"
			stonepickaxe.damage = 10
			player1.instrument[0].usage = 25
			player1.instrument[0].name = stonepickaxe.name	
		elif craftitem == "":
			a == None
		
#items
	for e in player1.instrument:
		if (player1.instrument[0].usage == None) or (player1.instrument[0].usage <= 0):
			player1.instrument.clear()
		
#iron
	
	for e in iron_mass:		
		if (u[0] == e[0]) and (u[1] == e[1]) and (player1.instrument[0].name == "stone pickaxe"):
			question = input("You are see a skin-colored metall... Y/N:")
			if question == "Y":
				print("Kick")
				input()
				print("Din'-Din'-Din'!")
				input()
				print("Hit!")
				input()
				print("Mining!")
				input()
				print("Finish him!")
				input()
				player1.instrument[0].usage -= 1
			iron_ore = item()
			iron_ore.id = 4
			iron_ore.name = "Iron Ore"
			question = input("You found Stone. Have you take it?Y/N")
			while question != "Y" and question != "N":
				question = input("On floor you see any items. Have you take it?Y/N")			
			if question == "Y":
				if (player1.inventories[0].k == 0):			
						player1.inventories[0].k = iron.k
						player1.inventories[0].name = iron.name
					
				elif (player1.inventories[0].k != 0) and (player1.inventories[1].k == 0):
						player1.inventories[1].k = iron.k
						player1.inventories[1].name = iron.name
							
				elif (player1.inventories[1].k != 0) and ((player1.inventories[2].k == 0)):

						player1.inventories[2].k = iron.k
						player1.inventories[2].name = iron.name

				elif (player1.inventories[2].k != 0) and (player1.inventories[3].k == 0):
						player1.inventories[3].k = iron.k
						player1.inventories[3].name = iron.name							
					
				elif (player1.inventories[3].k != 0) and (player1.inventories[4].k == 0):
						player1.inventories[4].k = iron.k
						player1.inventories[4].name = iron.name	
						
				if (player1.inventories[0].k != 0) and (player1.inventories[1].k != 0) and (player1.inventories[2].k != 0) and (player1.inventories[3].k != 0) and (player1.inventories[4].k != 0):
					player.inventories.append(iron)
				iron_ex == False
			
			if iron_ex == False:
				g_t_r = 0
				simp = len(iron_mass)
				iron_mass.remove(stones_mass[random.randrange(g_t_r, simp)])
				simp = 0
				iron_ex = True
				player1.x -= 1		
		
		if question == "N":
			a = None
#helpmanual
	
	if a == "h":
			print("##################---HELP---##################\n --Version--\n Alfa-0.2.1\n --credits--\n EndiFox - Developer\n\n ---MOVEMENT--\n w - up\n a - left\n s - down\n d - Right\n t - show my position\n e - show in-game time\n q - show time of day\n h - show this manual\n cr - craft mananger\n If you position is on 0 or lower 0 for X, you need press any button.\n ALERT! IN THIS VERSION YOU CANT SAVE GAME!\n##################---HELP---##################")
