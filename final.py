# This program uses human keys  down key  and left arrow key
# last change to line 2a

# how to launch and land a self-landing rocket.



# variables that user types in (real code):
massOfRocket = float(input("Enter mass of rocket in kg: "))
surfaceGravity = float(input("Enter surface gravity in m/s^2: "))
windSpeed = float(input("Enter wind speed in m/s: "))
landSpot = float(input("Where do you want the rocket to land on the X axis between 0 and 100 units: "))
finalAltitude = float(input("What do you want the max altitude of the rocket to be on the Y axis between 0 and 100 units: "))



# pseudo code variables:

# rocketFuel = int(100) # gets changed by rocket speed and other stuff later on



# Where does rocket need to reach finalAltitude on X axis (pseudo code):


# finalAltitudeXAxis = (50-rocketLandSpot)/2
# finalAltitudeCoordinates = (finalAltitude, finalAltitudeXAxis)



# Python algorithms figure out how to launch rocket safely (pseudo code):


# launchSpeed = something to do with surfaceGravity
# launchSpeed = launchSpeed+something to do with finalAltitudeCoordinates

# launchDirection = 0 (insert operator here) something to do with rocketLandSpot
# launchDirection = launchDirection (insert operator here) something to do with windSpeed
# launchDirection = launchDirection (insert operator here) something to do with finalAltitudeCoordinates



# Algorithm to get to finalAltitudeCoordinates (pseudo code):


# Launching:

# point rocket in launchDirection
# accelerate rocket to launchSpeed at some acceleration


# variables affecting rocket during mission to finalAltitudeCoordinates:

# while True:
# 	rocketWeight = float(something to do with current gravity and massOfRocket)
# 	rocketWeight = rocketWeight-something to do with rocketFuel
# 	rocketSpeed(undefined variable) = rocketSpeed+something to do with rocketWeight
#   windSpeed affects path of rocket (insert complex physics here)
# 	if (rocket moves in certain direction on x axis because of wind):
# 		use physics to change movement of rocket and change speed to get to finalAltitudeCoordinations
# 	if (rocketCoordinations(undefined variable) == some amount of units away from finalAltitudeCoordinations):
#  		break
# 	else:
# 		continue


# deccelerating rocket to finalAltitudeCoordinates:

# while True:
# 	deccelerationToFinalAltitude = something to do with current speed and how far away rocketCoordinations are from finalAltitudeCoordinations
# 	execute deccelerationToFinalAltitude
# 	if (rocketCoordinations == finalAltitudeCoordinations):
#  			break
# 		else:
# 			continue



# Algorithm to get to landing coordinates (pseudo code):


# variables:

# landSpotCoordinates = (rocketLandSpot, 0)
# landDirection = direction towards landSpotCoordinates
# rocketWeight = float(something to do with current gravity and massOfRocket)
# rocketWeight = rocketWeight-something to do with rocketFuel
# landSpeed = something to do with how landSpotCoordinates
# landSpeed = landSpeed and something to do with rocketWeight


# Starting landing:

# point rocket in landDirection
# accelerate rocket to landSpeed at some acceleration


# variables affecting rocket during mission to landSpotCoordinates:

# while True:
# 	rocketWeight = float(something to do with current gravity and massOfRocket)
# 	rocketWeight = rocketWeight-something to do with rocketFuel
# 	rocketSpeed(undefined variable) = rocketSpeed+something to do with rocketWeight
#   windSpeed affects path of rocket (insert complex physics here)
# 	if (rocket moves in certain direction on x axis because of wind):
# 		use physics to change movement of rocket and change speed to get to landSpotCoordinations
# 	if (rocketCoordinations(undefined variable) == some amount of units away from landSpotCoordinations):
# 		change rocket direction degrees to 0 degrees
#  		break
# 	else:
# 		continue


# deccelerating rocket to landSpotCoordinates:

# while True:
#	deccelerationToLandSpot = something to do with current speed and how far away rocketCoordinations are from landSpotCoordinations
# 	execute deccelerationToLandSpot
# 	if (rocketCoordinations == landSpotCoordinations):
#  			break
# 		else:
# 			continue



# graphics info:


# movement:

# when rocket moves horizontaly to fight wind show side stabilizers shoot out air
# when rocket speed goes faster show flame getting bigger on bottom


# Things that live sensor feedback will constantly update and tell you about (pseudo code):

# while True:
# 	print("Coordinates of rocket: " + str(rocketCoordinates))
# 	print("Velocity of rocket: " + str(rocket velocity))
# 	print("Acceleration of rocket: " + str(rocket acceleration))
# 	print("Force of gravity on rocket: " + str(current gravity))
# 	print("Weight of rocket: " + str(rocketWeight))
# 	print("Fuel left: " + str(fuel left))
# 	print("Angle of nose: " + str(rocket direction))
# 	print("Altitude of rocket: " + str(rocket altitude))
# 	print("Air pressure at current altitude: " + str(air pressure))
# 	if (rocketCoordinates == landSpotCoordinates):
# 		break
# 	else:
# 		delete all printed statements
# 		wait 0.1 seconds
# 		continue


# Stats after rocket lands:

# print("The rocket has landed succesfully!")
# print("Rocket weight at highest altitude: " + str(lowest weight))
# print("Gravity at highest altitude: " + str(lowest gravity))
# print("Highest air pressure: " + str(highest air pressure))
# print("Highest velocity of rocket: " + str(highest velocity))