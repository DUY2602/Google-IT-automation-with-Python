# Debug with print method

import urllib3

def get_web_page(url):
	http = urllib3.PoolManager()


	print("Retrieving URL:", url)
	response = http.request("GET", url)


	print("HTTP response code:", response.status, response.reason)
	print(response.data.decode("utf-8", errors="replace"))
	
get_web_page("http://google.com")
