from bs4 import BeautifulSoup
import requests

URL = 'https://www.scrapethissite.com/pages/forms/?page_num=1'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

   
team_name = soup.find_all('td', class_='name')
team_win = soup.find_all('td', class_='pct text-success')
team_goal = soup.find_all('td', class_='ga') 


for name, win, goal in zip(team_name, team_win, team_goal):
    print(name.text, '-', win.text, '-', goal.text)