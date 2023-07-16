import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'} 

def get_shopper_cities():
    URL = 'https://www.shoppersstop.com/store-finder'
    r = requests.get(URL, headers=headers)
    soup  = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='select-option')
    content = s.find_all('span')

    cities = []
    for line in content:
        cities.append(line.text)

    shopper_city_list = set(cities[0].splitlines())
    shopper_city_list.remove('')
    shopper_city_list.remove('Select City')
    return shopper_city_list

print(get_shopper_cities())
