import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/interestingasfuck/comments/9yr5t5/near_complete_remains_of_an_iron_age_horse_drawn/'

headers = {'User-Agent': 'Chrome/39.0.2171.95'}

response = requests.get(url, headers=headers)

username = re.findall(r"<a class=\"s1461iz-1 ffqGHT\" href=\"/user/[^\"]+\">([^<]+)</a>", response.text)

for match in username:
    print(username)
    print('\n')
