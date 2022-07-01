# import requests 
# from bs4 import BeautifulSoup
# URL = "https://www.geeksforgeeks.org/data-structures/"
# r = requests.get(URL)
# print(r.content)  

# import requests 
# from bs4 import BeautifulSoup
# URL = "https://www.python.org"
# r = requests.get(URL)
# print(r.content)

import requests 
from bs4 import BeautifulSoup
URL = "https://www.dataquest.io"
r = requests.get(URL)
print(r.content)