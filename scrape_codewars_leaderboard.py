# get all tr which have the data-username attributes
from bs4 import BeautifulSoup
import requests 

URL = "https://www.codewars.com/users/leaderboard"

class User:
    def __init__(self,name,clan,honor,rank):
        self.name = name 
        self.clan = clan 
        self.honor = honor 
        self.rank = rank

class Leaderboard:
    def __init__(self,html_content):
        self.position = self._generate_leaderboard(html_content)

    def _generate_leaderboard(self,html_content):
        users = []
        soup = BeautifulSoup(html_content,'html.parser')
        rows = soup.find_all('tr', attrs={'data-username': True})

        for row in rows[:3]:
            username = row.get('data-username')
            rank = row.find('td',class_='rank').text.strip('#')
            clan = row.find_all('td')[2].text.strip()
            honor = int(row.find('td',class_='honor').text.strip().replace(',',''))
            print('rank ',rank)
            print('clan ',clan)
            print('honor ',honor)
            print('username ',username)
            users.append(User(username,clan,honor,rank))
        
        return users


def solution():
    response = requests.get(URL)
    document = response.text
    return Leaderboard(document)

leaders_arr = solution()
for leader in leaders_arr.position:
    print(leader.name)
    print(leader.clan)
    print(leader.rank)
    print(leader.honor)

print(leaders_arr.position[0].name)