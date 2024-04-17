from bs4 import BeautifulSoup
import requests

URL = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
    
country_tags = soup.find_all('h3', class_='country-name')

for country in country_tags:
    print (country.name)
