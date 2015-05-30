import json
import csv
from brewerydb import *

BreweryDb.configure(API_KEY)
data = []

for i in range(835):
	try:
		data.append((BreweryDb.beers({'p':i+1, 'withBreweries':'Y'})))
		print("Extracted data on page " + str(i+1))
	except Exception:
		print("Error getting data on page " + str(i+1))
	
datalen = len(data)
errorCount = 0
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['beerName', 'beerStyle', 'createDate', 'BreweryName', 'locationType', 'StateName', 'countryISO'])
for y in range(datalen):
	for x in range(len(data[y]['data'])):
		try:
			beerName = data[y]['data'][x]['name']
			beerStyle = data[y]['data'][x]['style']['category']['name']
			createDate = data[y]['data'][x]['createDate']
			#glassName = data[y]['data'][x]['glass']['name']
			BreweryName = data[y]['data'][x]['breweries'][0]['name']
			locationType = data[y]['data'][x]['breweries'][0]['locations'][0]['locationTypeDisplay']
			StateName = data[y]['data'][x]['breweries'][0]['locations'][0]['region']
			countryISO = data[y]['data'][x]['breweries'][0]['locations'][0]['country']['isoCode']
			
			breweries = data[y]['data'][x]['breweries']
			numberOfBreweries = len(breweries)
			
			outputWriter.writerow([beerName, beerStyle, createDate, BreweryName, locationType, StateName, countryISO])
		except Exception:
			errorCount += 1
print('Program done. There were ' + str(errorCount) + ' output errors.')
