import requests
import csv
import codecs
from bs4 import BeautifulSoup

#Exception Handling
try:

	source = requests.get('https://winefolly.com/lifestyle/top-wine-regions-of-the-world/')
	source.raise_for_status()

	soup = BeautifulSoup(source.text, 'html.parser')
	regions = soup.find('div',class_="post-body prose content").find_all('h4')
	file = open('region.csv', 'w')
	writer = csv.writer(file)

	writer.writerow(['Country'])
	for region in regions:
		reg = region.text.strip()
		writer.writerow([reg])
	file.close()

except Exception as e:
	print(e)
