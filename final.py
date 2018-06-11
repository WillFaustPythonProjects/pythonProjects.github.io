import math

def dayOfWeek():
	mInitial=input("What month were you born? Enter Name of month: ") # month number
	m=0

	k=int(input("What day of the month were you born?: ")) # date

	y=int(input("What year were you born?: ")) # year

	march=1

	april=2

	may=3

	june=4

	july=5

	august=6

	september=7

	october=8

	november=9

	december=10

	january=11

	february=12

	if (mInitial == str("march")):
		m=march
	elif (mInitial == str("March")):
		m=march

	if (mInitial == str("april")):
		m=april
	elif (mInitial == str("April")):
		m=april
	
	if (mInitial == str("may")):
		m=may
	elif (mInitial == str("May")):
		m=may
	
	if (mInitial == str("june")):
		m=june
	elif (mInitial == str("June")):
		m=june
	
	if (mInitial == str("july")):
		m=july
	elif (mInitial == str("July")):
		m=july
	
	if (mInitial == str("august")):
		m=august
	elif (mInitial == str("August")):
		m=august
	
	if (mInitial == str("september")):
		m=september
	elif (mInitial == str("September")):
		m=september
	
	if (mInitial == str("october")):
		m=october
	elif (mInitial == str("October")):
		m=october
	
	if (mInitial == str("november")):
		m=november
	elif (mInitial == str("November")):
		m=november
	
	if (mInitial == str("december")):
		m=december
	elif (mInitial == str("December")):
		m=december
		
	if (mInitial == str("january")):
		m=january
	elif (mInitial == str("January")):
		m=january
	
	if (mInitial == str("february")):
		m=february
	elif (mInitial == str("February")):
		m=february

	c=int(math.trunc(y/100))

	d=int(y%100)

	fnum=(k + math.trunc((13*m-1)/5) + d + math.trunc(d/4) + math.trunc(c/4) - 2*c)%7
	f=""
	
	if (fnum == 0):
		f="Sunday"

	if (fnum == 1):
		f="Monday"
		
	if (fnum == 2):
		f="Tuesday"
		
	if (fnum == 3):
		f="Wednesday"
		
	if (fnum == 4):
		f="Thursday"
		
	if (fnum == 5):
		f="Friday"
		
	if (fnum == 6):
		f="Saturday"

	print("")
	print("you were born on "+f+".")



dayOfWeek()