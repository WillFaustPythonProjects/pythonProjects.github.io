a1="-"
a2="-"
a3="-"
a4="-"
a5="-"
a6="-"
a7="-"
a8="-"
a9="-"
    

def myMove():
    print("")
    print("Ok, I'm gonna move here...")
    
def yourMove():
    print("Your move...")

def printGrid():
    print(a1+" "+a2+" "+a3)
    print(a4+" "+a5+" "+a6)
    print(a7+" "+a8+" "+a9)

print("Let's play tic-tac-toe!")
print("My turn first! I'm 'X'.")
a7="X"
printGrid()

user=input("Where would you like to put your first 'O'? (1-9 from left to right): ")

if (user=="8"): # first possibility win strategy
    a8="O"
    yourMove()
    printGrid()
    myMove()
    a5="X"
    printGrid()
    print("")
    user=input("Where would you like to put your second 'O'? (1-9 from left to right): ")
    if (user=="3"):
        a3="O"
        yourMove()
        printGrid()
        myMove()
        a1="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="4"):
            a4="O"
            yourMove()
            printGrid()
            a9="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        elif (user=="9"):
            a9="O"
            yourMove()
            printGrid()
            a4="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        else:
            if (user=="2"):
                a2="O"
            if (user=="6"):
                a6="O"
            yourMove()
            printGrid()
            myMove()
            a9="X"
            printGrid()
            print("I win! 3 in a row!")
            
    else:
        if (user=="1"):
            a1="O"
        if (user=="2"):
            a2="O"
        if (user=="4"):
            a4="O"
        if (user=="6"):
            a6="O"
        if (user=="9"):
            a9="O"
        yourMove()
        printGrid()
        myMove()
        a3="X"
        printGrid()
        print("I win! 3 in a row!")
    user="a"
        
if (user=="9"): # second possibility win strategy
    a9="O"
    yourMove()
    printGrid()
    myMove()
    a3="X"
    printGrid()
    print("")
    user=input("Where would you like to put your second 'O'? (1-9 from left to right): ")
    if (user=="5"):
        a5="O"
        yourMove()
        printGrid()
        myMove()
        a1="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="2"):
            a2="O"
            yourMove()
            printGrid()
            a4="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        elif (user=="4"):
            a4="O"
            yourMove()
            printGrid()
            a2="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        else:
            if (user=="6"):
                a6="O"
            if (user=="8"):
                a8="O"
            yourMove()
            printGrid()
            myMove()
            a2="X"
            printGrid()
            print("I win! 3 in a row!")
    else:
        if (user=="1"):
            a1="O"
        if (user=="2"):
            a2="O"
        if (user=="4"):
            a4="O"
        if (user=="6"):
            a6="O"
        if (user=="8"):
            a8="O"
        yourMove()
        printGrid()
        myMove()
        a5="X"
        printGrid()
        print("I win! 3 in a row!")
    user="a"
        
if (user=="6"): # third possibility win strategy
    a6="O"
    yourMove()
    printGrid()
    myMove()
    a5="X"
    printGrid()
    print("")
    user=input("Where would you like to put your second 'O'? (1-9 from left to right): ")
    if (user=="3"):
        a3="O"
        yourMove()
        printGrid()
        myMove()
        a9="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="1"):
            a1="O"
            yourMove()
            printGrid()
            a8="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        elif (user=="8"):
            a8="O"
            yourMove()
            printGrid()
            a1="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        else:
            if (user=="2"):
                a2="O"
            if (user=="4"):
                a4="O"
            yourMove()
            printGrid()
            myMove()
            a8="X"
            printGrid()
            print("I win! 3 in a row!")
    else:
        if (user=="1"):
            a1="O"
        if (user=="2"):
            a2="O"
        if (user=="4"):
            a4="O"
        if (user=="8"):
            a8="O"
        if (user=="9"):
            a9="O"
        yourMove()
        printGrid()
        myMove()
        a3="X"
        printGrid()
        print("I win! 3 in a row!")
    user="a"
        
if (user=="3"): # fourth possibility win strategy
    a3="O"
    yourMove()
    printGrid()
    myMove()
    a9="X"
    printGrid()
    print("")
    user=input("Where would you like to put your second 'O'? (1-9 from left to right): ")
    if (user=="8"):
        a8="O"
        yourMove()
        printGrid()
        myMove()
        a1="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="4"):
            a4="O"
            yourMove()
            printGrid()
            a5="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        elif (user=="5"):
            a5="O"
            yourMove()
            printGrid()
            a4="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        else:
            if (user=="2"):
                a2="O"
            if (user=="6"):
                a6="O"
            yourMove()
            printGrid()
            myMove()
            a4="X"
            printGrid()
            print("I win! 3 in a row!")
    else:
        if (user=="1"):
            a1="O"
        if (user=="2"):
            a2="O"
        if (user=="4"):
            a4="O"
        if (user=="5"):
            a5="O"
        if (user=="6"):
            a6="O"
        yourMove()
        printGrid()
        myMove()
        a8="X"
        printGrid()
        print("I win! 3 in a row!")
    user="a"
        
if (user=="2"): # fifth possibility win strategy
    a2="O"
    yourMove()
    printGrid()
    myMove()
    a5="X"
    printGrid()
    print("")
    user=input("Where would you like to put your second 'O'? (1-9 from left to right): ")
    if (user=="3"):
        a3="O"
        yourMove()
        printGrid()
        myMove()
        a1="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="4"):
            a4="O"
            yourMove()
            printGrid()
            a9="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        elif (user=="9"):
            a9="O"
            yourMove()
            printGrid()
            a4="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        else:
            if (user=="6"):
                a6="O"
            if (user=="8"):
                a8="O"
            yourMove()
            printGrid()
            myMove()
            a4="X"
            printGrid()
            print("I win! 3 in a row!")
    else:
        if (user=="1"):
            a1="O"
        if (user=="4"):
            a4="O"
        if (user=="6"):
            a6="O"
        if (user=="8"):
            a8="O"
        if (user=="9"):
            a9="O"
        yourMove()
        printGrid()
        myMove()
        a3="X"
        printGrid()
        print("I win! 3 in a row!")
    user="a"
        
if (user=="1"): # sixth possibility win strategy
    a1="O"
    yourMove()
    printGrid()
    myMove()
    a3="X"
    printGrid()
    print("")
    user=input("Where would you like to put your second 'O'? (1-9 from left to right): ")
    if (user=="5"):
        a5="O"
        yourMove()
        printGrid()
        myMove()
        a1="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="2"):
            a2="O"
            yourMove()
            printGrid()
            a4="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        elif (user=="4"):
            a4="O"
            yourMove()
            printGrid()
            a2="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        else:
            if (user=="6"):
                a6="O"
            if (user=="8"):
                a8="O"
            if (user=="9"):
                a9="O"
            yourMove()
            printGrid()
            myMove()
            a4="X"
            printGrid()
            print("I win! 3 in a row!")
    else:
        if (user=="2"):
            a2="O"
        if (user=="4"):
            a4="O"
        if (user=="6"):
            a6="O"
        if (user=="8"):
            a8="O"
        if (user=="9"):
            a9="O"
        yourMove()
        printGrid()
        myMove()
        a5="X"
        printGrid()
        print("I win! 3 in a row!")
    user="a" 
        
if (user=="4"): # seventh possibility win strategy
    a4="O"
    yourMove()
    printGrid()
    myMove()
    a5="X"
    printGrid()
    print("")
    user=input("Where would you like to put your second 'O'? (1-9 from left to right): ")
    if (user=="3"):
        a3="O"
        yourMove()
        printGrid()
        myMove()
        a9="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="1"):
            a1="O"
            yourMove()
            printGrid()
            a8="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        elif (user=="8"):
            a8="O"
            yourMove()
            printGrid()
            a1="X"
            myMove()
            printGrid()
            print("I win! 3 in a row!")
        else:
            if (user=="2"):
                a2="O"
            if (user=="6"):
                a6="O"
            yourMove()
            printGrid()
            myMove()
            a8="X"
            printGrid()
            print("I win! 3 in a row!")
    else:
        if (user=="1"):
            a1="O"
        if (user=="2"):
            a2="O"
        if (user=="6"):
            a6="O"
        if (user=="8"):
            a8="O"
        if (user=="9"):
            a9="O"
        yourMove()
        printGrid()
        myMove()
        a3="X"
        printGrid()
        print("I win! 3 in a row!")
    user="a"
        
if (user=="5"): # eigth possibility win strategy
    a5="O"
    yourMove()
    printGrid()
    myMove()
    a3="X"
    printGrid()
    print("")
    user=input("Where would you like to put your second 'O'? (1-9 from left to right): ")
    
    if (user=="2"): # if user goes to '2' to tie
        a2="O"
        yourMove()
        printGrid()
        myMove()
        a8="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="9"):
            a9="O"
            yourMove()
            printGrid()
            myMove()
            a1="X"
            printGrid()
            user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
            if (user=="4"):
                a4="O"
                yourMove()
                printGrid()
                myMove()
                a6="X"
                printGrid()
                print("It's a tie! Nice job!")
            else:
                if (user=="6"):
                    a6="O"
                    yourMove()
                    printGrid()
                    myMove()
                    a4="X"
                    printGrid()
                    print("I win! 3 in a row!")
        else:
            if (user=="1"):
                a1="O"
            if (user=="4"):
                a4="O"
            if (user=="6"):
                a6="O"
            yourMove()
            printGrid()
            myMove()
            a9="X"
            printGrid()
            print("I win! 3 in a row!")
        user="a"
            
    if (user=="8"): # if user goes to '8' to tie
        a8="O"
        yourMove()
        printGrid()
        myMove()
        a2="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="1"):
            a1="O"
            yourMove()
            printGrid()
            myMove()
            a9="X"
            printGrid()
            user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
            if (user=="6"):
                a6="O"
                yourMove()
                printGrid()
                myMove()
                a4="X"
                printGrid()
                print("It's a tie! Nice job!")
            else:
                if (user=="4"):
                    a4="O"
                    yourMove()
                    printGrid()
                    myMove()
                    a6="X"
                    printGrid()
                    print("I win! 3 in a row!")
        else:
            if (user=="4"):
                a4="O"
            if (user=="6"):
                a6="O"
            if (user=="9"):
                a9="O"
            yourMove()
            printGrid()
            myMove()
            a1="X"
            printGrid()
            print("I win! 3 in a row!")
        user="a"
            
    if (user=="4"): # if user goes to '4' to tie
        a4="O"
        yourMove()
        printGrid()
        myMove()
        a6="X"
        printGrid()
        print("")
        user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
        if (user=="9"):
            a9="O"
            yourMove()
            printGrid()
            myMove()
            a1="X"
            printGrid()
            user=input("Where would you like to put your third 'O'? (1-9 from left to right): ")
            if (user=="2"):
                a2="O"
                yourMove()
                printGrid()
                myMove()
                a8="X"
                printGrid()
                print("It's a tie! Nice job!")
            else:
                if (user=="8"):
                    a8="O"
                    yourMove()
                    printGrid()
                    myMove()
                    a2="X"
                    printGrid()
                    print("I win! 3 in a row!")
        else:
            if (user=="1"):
                a1="O"
            if (user=="2"):
                a2="O"
            if (user=="8"):
                a8="O"
            yourMove()
            printGrid()
            myMove()
            a9="X"
            printGrid()
            print("I win! 3 in a row!")
        user="a"
