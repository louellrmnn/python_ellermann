from bs4 import BeautifulSoup
import requests

URL = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')
    
country_tags = soup.find_all('h3', class_='country-name')
country_infos = soup.find_all('span', class_='country-capital')
 
for country, capital in zip(country_tags, country_infos):
    print(country.text, '-', capital.text)