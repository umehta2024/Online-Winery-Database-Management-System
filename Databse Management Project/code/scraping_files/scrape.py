import requests
import csv
import codecs
from bs4 import BeautifulSoup

#Exception Handling
try:

	source = requests.get('https://top100.winespectator.com/lists/')
	source.raise_for_status()

	soup = BeautifulSoup(source.text, 'html.parser')
	wines = soup.find('tbody').find_all('tr')
	file = open('winedata.csv', 'w')
	writer = csv.writer(file)
	
	writer.writerow(['Wine Name','Price','Score'])
	for wine in wines:
		name = wine.find('td',class_="name").find('div',class_="table-name").find('span',class_="wineName").find_next('span').text.strip()
		price = wine.find('td',class_="price").text.strip()
		score = wine.find('td',class_="score").text.strip()
		writer.writerow([name,price,score])
	file.close()


except Exception as e:
	print(e)

# Result will be stored in a File called winedata.csv
# Some Characters are not coming in, but we can fix it (They are just French Accent Characters)
