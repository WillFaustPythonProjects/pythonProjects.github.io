import requests
import lxml.html
while True:
	html = requests.get('https://newegg.com/amd-ryzen-5-5600x/p/N82E16819113666')
	site = lxml.html.fromstring(html.content)
	try:
		print(site.xpath('//*[@class="nav-col"]/span/text()')[0])
	except IndexError:
		print("In stock")