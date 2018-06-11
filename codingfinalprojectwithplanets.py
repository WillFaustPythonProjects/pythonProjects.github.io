def rockCalc():	
	planet=input("What planet did you drop the rock from? (list one of the 8 official planets or our moon): ")
	if (planet=="Earth"):
	    a=9.8
	elif (planet=="Moon"):
	    a=1.62
	elif (planet=="Mercury"):
	    a=3.7
	elif (planet=="Venus"):
	    a=8.87
	elif (planet=="Jupiter"):
	    a=24.79
	elif (planet=="Saturn"):
	    a=10.44
	elif (planet=="Uranus"):
	    a=8.87
	elif (planet=="Neptune"):
	    a=11.15
	elif (planet=="Mars"):
	    a=3.71
	else:
	    print("I don't know what you mean.  Let's just do Earth")
	    a=9.8
	    
	print("")
	d=float(input("How high was the rock dropped off the ground in meters?: "))
	t=float(((2*d)/a)**0.5)
	v=float(a*t)
	print("")
	print("")
	print("The rock that was dropped from "+str(round(d, 2))+" meters off the ground")
	print("took "+str(round(t, 2))+" seconds to reach the ground.")
	print("")
	print("The rock was traveling at "+str(round(v, 2))+" meters per second right before it hit the ground.")

while True:
	rockCalc()
	print("")
	again=input("Would you like to calculate again using a different distance or planet? (yes or no): ")
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