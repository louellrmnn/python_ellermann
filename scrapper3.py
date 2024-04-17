from bs4 import BeautifulSoup
import requests

URL = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
