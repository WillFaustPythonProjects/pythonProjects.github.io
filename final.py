"""
This program asks you various questions and gives
clever answers in return
"""

import math # imports the math library into my program


def dayOfWeek(): # this function figures out the day of the week you were born
	print("")
	print("")
	mInitial=input("What month were you born? Enter Name of month: ") # month number
	m=0

	k=int(input("What day of the month were you born?: ")) # date

	y=int(input("What year were you born?: ")) # year

    # all these variables below assign different months to numbers...
    
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

    # all of the if statements below assign what month you typed in
    # earlier to the right number

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

	c=int(math.trunc(y/100)) # this figures out the first 2 digits of the year you enetered

	d=int(y%100) # this figures out the last 2 digits of the year you entered

    # the equation below figures out what day of the week you were born
    # based on the variables k (day of month), m (what month you typed in),
    # c (the first 2 digits of the year), and d (the last 2 digits of the year)

	fnum=(k + math.trunc((13*m-1)/5) + d + math.trunc(d/4) + math.trunc(c/4) - 2*c)%7
	f=""
	
	# the if statements below convert fnum (a number) to f (a string)
	
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
	print("you were born on "+f+".") # this tells you what day of the week you were born


# the code below has you make a password and asks you some questions
while True: 
    on_button = input("Type 'turn on' to turn on machine: ")
    if (on_button == "turn on"):
        print("Machine is now on!")
            
        password = input("Choose a password: ") # password made here
            
        print("Welcome! ;)")
                
        fav_num = int(input("What is your favorite number?: ")) # asks favorite number
        print("Cool!")    
                
        while True:
            pass_input = input("Type your password and I will tell you my favorite number: ")
            if (pass_input == password):
                print("")
                print("My favorite number is better than yours! Mine is " + str(fav_num + 1) + "!")
                break
            else:
                print("Access denied...Try again...")
                continue # if you don't get password right you try again until you do
        break
    else:
        print("'machine sleeping... zzz'")
        continue # if you don't type "turn on" you can try again until you do


dayOfWeek() # calls this function

print("")
print("Thank you for completing this survey!")
print("We have already sent your information")
print("to over one hundred million advertisers!")
