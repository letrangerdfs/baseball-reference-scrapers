import requests
from bs4 import BeautifulSoup

url = 'https://www.baseball-reference.com/leagues/majors/2022-schedule.shtml'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a', href=lambda href: href and '/boxes/' in href and href.endswith('.shtml'))

base_url = 'https://www.baseball-reference.com'
full_links = [base_url + link['href'] for link in links]

for full_link in full_links:
    print(full_link)