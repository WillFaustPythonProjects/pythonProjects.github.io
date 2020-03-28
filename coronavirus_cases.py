#Imports required libraries for this project
import requests
import lxml.html
from datetime import date
import re

# Main function/program
def coronavirus_cases():

  # Grabs current day of the month.
  current_date = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/div[3]/span[@class="last x-label svelte-2xhdfr"]/text()')[0]
  current_day = re.sub('[a-z, A-Z]', '', current_date)
  current_day = current_day[1:]

  while True:
    
    # Asks user for a valid date.
    print("")
    date_string = input("Type in a date and you can see how many new coronavirus cases were reported that day in the United States. Choose any date from February 26 to today (March "+str(current_day)+"): ")

    # Stores the day and month entered by the user in two variables.
    day = re.sub('[a-z, A-Z]', '', date_string)
    month = re.sub('[0-9]', '', date_string)

    # Checks if user-entered date is valid.
    if (month=="February " and int(day)<=29 and int(day)>=26):
      month_num=2
      break
    elif (month=="March " and int(day)<=int(current_day) and int(day)>=1):
      month_num=3
      break
    else:
      print("Not a valid date. Try again.")
      continue

  # Figures out how many days the virus has been in the U.S. since The New York Times' current earliest record.
  d0 = date(2020, 2, 26)
  d1 = date(2020, int(month_num), int(day))
  delta = d1 - d0
  virus_day_num = delta.days+1

  # Calculates how many new cases were reported on the user-entered date.
  fifteen_cases_height = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/svg/rect[1]/@height')[0]
  new_cases_height = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/svg/rect['+str(virus_day_num)+']/@height')[0]
  new_cases = float(new_cases_height)/(float(fifteen_cases_height)/15)

  # Prints how many new cases were reported on the user-entered date.
  print(str(round(new_cases)))

# Grabs a New York Times page that contains the current total cases in the U.S.
html = requests.get('https://www.nytimes.com/interactive/2020/world/coronavirus-maps.html')
doc = lxml.html.fromstring(html.content)

# Grabs the current total cases in the U.S.
total_cases = doc.xpath('//*[@id="heatmap"]/div[1]/table/tbody/tr[1]/td[2]/text()')[0]

# Prints the current total cases in the U.S.
print("Total coronavirus cases in the United States: "+str(total_cases))

# Grabs the main New York Times page that contains how many new cases were reported each day in the U.S. since their current earliest record.
html = requests.get('https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html')
doc = lxml.html.fromstring(html.content)

# Runs the main function/program, asks if you want data for another date, and either runs the program again or quits.
while True:
  coronavirus_cases()
  print("")
  rerun = input("Would you like to try another date? ('y' or 'n')")
  if (rerun=="y"):
    continue
  elif (rerun=="n"):
    print("Ok, quitting.")
    break
  else:
    print("Not a valid answer, quitting.")
    break
