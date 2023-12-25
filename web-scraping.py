# One of the most valuable skills of a developer is Web scraping. 
# In this project, you will scrape your GitHub profile image. 
# note that basic knowledge of html and the request and BeautifulSoup libraries in Python is required

# install the beautifulsoup4
# 'pip install beautifulsoup4'. the request library is usually already present in python std lib

import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/chimezdev"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_pic = scraper.find("img", {"alt": "Avatar"})
print(profile_pic)
