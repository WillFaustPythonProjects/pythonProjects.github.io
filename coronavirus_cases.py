import requests
import lxml.html
from datetime import date
import re

html = requests.get('https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html')
doc = lxml.html.fromstring(html.content)

current_date = doc.xpath('//*[@id="interactive-byline"]/time/text()[2]')[0]
current_day = re.sub('[a-z, A-Z]', '', current_date)
current_day = current_day[:2]

while True:
  date_string = input("Type in a date and you can see how many coronavirus cases were reported that day in the United States. Choose any date from January 21 to today (March "+str(current_day)+"): ")

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

one_case_height = doc.xpath('//*[@id="g-trajectory"]/div[1]/div/div/svg/rect[1]/@height')[0]
new_cases_height = doc.xpath('//*[@id="g-trajectory"]/div[1]/div/div/svg/rect['+str(virus_day_num)+']/@height')[0]
new_cases = float(new_cases_height)/float(one_case_height)

print(str(round(new_cases)))