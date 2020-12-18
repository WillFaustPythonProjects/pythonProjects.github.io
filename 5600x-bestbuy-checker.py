import lxml.html
import requests
import time
from notify_run import Notify
from win10toast import ToastNotifier

n = 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}

while True:
  try:
    html = requests.get('https://bestbuy.com/site/amd-ryzen-5-5600x-4th-gen-6-core-12-threads-unlocked-desktop-processor-with-wraith-stealth-cooler/6438943.p',headers=headers).text
    site = lxml.html.fromstring(html)
  except lxml.etree.ParserError:
    time.sleep(1)
    continue

  try:
    status = site.xpath('//*[@class="fulfillment-add-to-cart-button"]/div/div/button/text()')[0]
  except IndexError:
    print(str(n) + ". IndexError, retrying")
    n = n + 1
    time.sleep(2)
    continue

  if (status == "Sold Out"):
    print(str(n) + ". Out of stock")
    n = n + 1
    continue
  elif (status == "Add to Cart"):
    print(str(n) + ". In stock")
    ToastNotifier().show_toast("5600x Bestbuy Checker:","The 5600x is in stock!",icon_path="ryzen.ico")
    Notify().send('The 5600x is in stock at Bestbuy!')
    n = n + 1
    continue
  else:
    print(str(n) + ". " + status)
    n = n + 1
    time.sleep(2)