# stock_scraper.py
# SOURCE

# cannot import name 'escape' from 'jinja2'
import csv
import requests
import black


# TODO refactor to scraping supplier website
URL = "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download"


# TODO refactor to scraping supplier, competitor and industry data websites
def get_data():
	r = requests.get(URL)
	data = r.text
	# TODO look to move WEBSCRAPE_000_RESULTS to pyproject.TOML
	WEBSCRAPE_000_RESULTS = {'children': []}
	for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
		WEBSCRAPE_000_RESULTS['children'].append({
			'name': line['Name'],
			'symbol': line['Symbol'],
			'price': line['lastsale'],
			'net_change': line['netchange'],
			'percent_change': line['pctchange'],
			'volume': line['share_volume'],
			'value': line['Nasdaq100_points']
		})
	return WEBSCRAPE_000_RESULTS
