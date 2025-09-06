# Debug with print method: Can see the current process at the time the program crashes 

import urllib3

def get_web_page(url):
	http = urllib3.PoolManager()


	print("Retrieving URL:", url)
	response = http.request("GET", url)


	print("HTTP response code:", response.status, response.reason)
	print(response.data.decode("utf-8"))
	
get_web_page("http://google.com")
