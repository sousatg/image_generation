import requests
import csv
from lxml import etree

fh = open( 'frases.csv', 'wb' )
csvWrite = csv.writer(fh, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

menuLinks = []
r = requests.get( 'http://www.frasescurtas.net/' )
if r.status_code == 200:
	html = r.content
	pageObj = etree.HTML( html )

	for menuItem in pageObj.xpath( '//*[@id="Mod114"]/div/div/ul/li/a' ):
		menuItemText = menuItem.xpath( './text()' )[0]
		menuItemHref = menuItem.xpath( './@href' )[0]
		menuLinks.append( { 'nome': menuItemText, 'href' : menuItemHref} )

for page in menuLinks:
	url = 'http://www.frasescurtas.net' + page['href']
	r = requests.get( url )
	if r.status_code == 200:
		html = r.content

		pageObj = etree.HTML( html )
		for frase in pageObj.xpath('//font/text()'):
			tmpfrase = ''.join( frase ).strip()
			if len(tmpfrase) > 5:
				csvWrite.writerow( [ frase.encode("utf-8"), page['nome'].encode("utf-8") ] )

fh.close()