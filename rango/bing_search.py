import json
import urllib, urllib2
from py_ms_cognitive import PyMsCognitiveWebSearch

def read_bing_key():
	bing_api_key = None

	try:
		with open('bing.key', 'r') as f:
			bing_api_key = f.readline()
	except:
		raise IOError('bing.key file not found')

	return bing_api_key

def run_query(search_terms):
	bing_api_key = read_bing_key()

	if not bing_api_key:
		raise KeyError("Bing Key Not Found")

	search_service = PyMsCognitiveWebSearch(bing_api_key, search_terms)
	first_fifty_result = search_service.search(limit=50, format='json')	

	print(first_fifty_result[0].title)
	print(first_fifty_result[0].display_url)
	print(first_fifty_result[0].snippet)
	return first_fifty_result



def main():
	query = raw_input('Please enter the query:')
	results = run_query(query)
	
if __name__ == '__main__':
	main()