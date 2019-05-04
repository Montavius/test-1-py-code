import random

userPick = int(input("Choose your item! Enter 0 for rock,1 for paper,2 for scissors"))
pcPick = random.randint (0,2)

#tie

if userPick==0 and pcPick==0
	print ("the champion picked ", pcPick," and you picked ",userPick,"to !?!?! TIE!") 
elif userPick==1 and pcPick==1
	print ("the champion picked ", pcPick," and you picked ",userPick,"to !?!?! TIE!") 
elif userPick==2 and pcPick==2
	print ("the champion picked ", pcPick," and you picked ",userPick,"to !?!?! TIE!") 

#you win

elif userPick==0 and pcPick==2
	print ("the champion picked ", pcPick," and you picked ",userPick,"YOU WIN !!!") 
elif userPick==1 and pcPick==0
	print ("the champion picked ", pcPick," and you picked ",userPick,"YOU WIN !!!") 
elif userPick==2 and pcPick==1
	print ("the champion picked ", pcPick," and you picked ",userPick,"YOU WIN !!!") 
#you lose

elif userPick==2 and pcPick==0
	print ("the champion picked ", pcPick," and you picked ",userPick,"YOU LOSE !!!") 
elif userPick==0 and pcPick==1
	print ("the champion picked ", pcPick," and you picked ",userPick,"YOU LOSE !!!") 
elif userPick==1 and pcPick==2
	print ("the champion picked ", pcPick," and you picked ",userPick,"YOU LOSE !!!") 