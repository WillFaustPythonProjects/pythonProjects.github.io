def rockCalc():	
	d=float(input("How high was the rock dropped off the ground in meters?: "))
	t=float(((2*d)/9.8)**0.5)
	v=float(9.8*t)
	print("")
	print("")
	print("The rock that was dropped from "+str(round(d, 2))+" meters off the ground")
	print("took "+str(round(t, 2))+" seconds to reach the ground.")
	print("")
	print("The rock was traveling at "+str(round(v, 2))+" meters per second right before it hit the ground.")

while True:
	rockCalc()
	print("")
	again=input("Would you like to calculate again using a different distance? (yes or no): ")
	if (again=="yes"):
		print("")
		print("")
		continue
	elif (again=="Yes"):
		print("")
		print("")
		continue
	elif (again=="no"):
		print("")
		print("Okay. Bye!")
		break
	elif (again=="No"):
		print("")
		print("Okay. Bye!")
		break
	else:
		print("")
		print("I don't know what you mean. Bye!")
		break