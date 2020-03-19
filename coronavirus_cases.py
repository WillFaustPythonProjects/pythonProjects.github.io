import requests
import lxml.html
from datetime import date
import re

html = requests.get('https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html')
doc = lxml.html.fromstring(html.content)


def coronavirus_cases():

  current_date = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/div[3]/span[@class="last x-label svelte-2xhdfr"]/text()')[0]
  current_day = re.sub('[a-z, A-Z]', '', current_date)
  current_day = current_day[1:]

  while True:
    print("")
    date_string = input("Type in a date and you can see how many new coronavirus cases were reported that day in the United States. Choose any date from January 21 to today (March "+str(current_day)+"): ")

    day = re.sub('[a-z, A-Z]', '', date_string)
    month = re.sub('[0-9]', '', date_string)

    if (month=="January " and int(day)<=31 and int(day)>=21):
      month_num=1
      break
    elif (month=="February " and int(day)<=29 and int(day)>=1):
      month_num=2
      break
    elif (month=="March " and int(day)<=int(current_day) and int(day)>=1):
      month_num=3
      break
    else:
      print("Not a valid date. Try again.")
      continue

  d0 = date(2020, 1, 21)
  d1 = date(2020, int(month_num), int(day))
  delta = d1 - d0
  virus_day_num = delta.days+1

  one_case_height = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/svg/rect[1]/@height')[0]
  new_cases_height = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/svg/rect['+str(virus_day_num)+']/@height')[0]
  new_cases = float(new_cases_height)/float(one_case_height)

  print(str(round(new_cases)))


current_date = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/div[3]/span[@class="last x-label svelte-2xhdfr"]/text()')[0]
current_day = re.sub('[a-z, A-Z]', '', current_date)
current_day = current_day[1:]

d0 = date(2020, 1, 21)
d1 = date(2020, 3, int(current_day))
delta = d1 - d0
day_in_loop = delta.days+1

one_case_height = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/svg/rect[1]/@height')[0]

total_cases = 0

while int(day_in_loop) != 0:
	new_cases_height = doc.xpath('//*[@id="g-cases-over-time"]/div[1]/div/div/svg/rect['+str(day_in_loop)+']/@height')[0]
	new_cases = float(new_cases_height)/float(one_case_height)
	new_cases = int(round(new_cases))
	day_in_loop = day_in_loop-1
	total_cases = total_cases+new_cases

print("Total coronavirus cases in the United States: "+str(total_cases))

while True:
  coronavirus_cases()
  print("")
  rerun = input("would you like to try another date? ('y' or 'n')")
  if (rerun=="y"):
    continue
  elif (rerun=="n"):
    print("Ok, quitting.")
    break
  else:
    print("Not a valid answer, quitting.")
    break
