import lxml.html
from urllib.request import urlopen
import time
from notify_run import Notify
from win10toast import ToastNotifier

n = 1

while True:
  try:
    html = urlopen('https://www.newegg.com/amd-ryzen-5-5600x/p/N82E16819113666').read().decode("utf-8")
    site = lxml.html.fromstring(html)
  except lxml.etree.ParserError:
    time.sleep(1)
    continue

  try:
    status = site.xpath('//*[@class="nav-col"]/descendant::node()/text()')[0]
  except IndexError:
    print(str(n) + ". IndexError, retrying")
    n = n + 1
    time.sleep(2)
    continue

  if (status == "Sold Out"):
    print(str(n) + ". Out of stock")
    n = n + 1
    continue
  elif (status == "Add to cart "):
    print(str(n) + ". In stock")
    ToastNotifier().show_toast("5600x Newegg Checker:","The 5600x is in stock!",icon_path="ryzen.ico")
    Notify().send('The 5600x is in stock!')
    n = n + 1
    continue
  else:
    print(str(n) + status)
    n = n + 1
    time.sleep(2)