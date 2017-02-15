import json
import urllib, urllib2

def read_bing_key():
	bing_api_key = None

	try:
		with open('bing.key', 'r') as f:
			bing_api_key = f.readline()
	except:
		raise IOError('bing.key file not found')

	return bing_api_key

def run_query(search_terms):
	bing_api_key = read_bing_key

	if not bing_api_key:
		raise KeyError("Bing Key Not Found")

	root_url = 'https://api.cognitive.microsoft.com/bing/v5.0/search/'
	service = 'Web'

	results_per_page = 10
	offset = 0