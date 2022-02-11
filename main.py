import requests
from bs4 import BeautifulSoup as bs
from lxml import html
from pprint import pprint
from datetime import datetime
import re

from random import choice
from fake_useragent import UserAgent

def get_user_agent():
    ua = UserAgent().random
    user_agent = {
        'User-Agent' : f'{ua}'
    }
    return user_agent

def osnovnoe():
    headers = get_user_agent()
    URL = 'https://habr.com'
    get_url = URL + '/ru/all/'
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    check = '(?:{})'.format('|'.join(KEYWORDS))
    response = requests.get(url = get_url, headers = headers)
    soup = bs(response.text,'lxml')
    for stat in soup.find_all('article'):
        date = datetime.strptime(stat.find('time').get('datetime'),"%Y-%m-%dT%H:%M:%S.%fZ")
        head = stat.find('h2').find('a')
        link = URL + head.get('href').strip()
        name = head.find('span').text.strip()
        if bool(re.search(check, name, flags=re.I)) == True:
            print(f'''Дата создания {date}
Заголовок {name}
Ссылка {link}''')
            print()

def facultativcik():
    headers = get_user_agent()
    URL = 'https://habr.com'
    get_url = URL + '/ru/all/'
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    check = '(?:{})'.format('|'.join(KEYWORDS))
    response = requests.get(url = get_url, headers = headers)
    soup = bs(response.text,'lxml')
    for stat in soup.find_all('article'):
        date = datetime.strptime(stat.find('time').get('datetime'),"%Y-%m-%dT%H:%M:%S.%fZ")
        head = stat.find('h2').find('a')
        link = URL + head.get('href').strip()
        name = head.find('span').text.strip()
        response2 = requests.get(url = link, headers = headers)
        soup2 = bs(response2.text,'lxml')
        text_stat = ''
        for text in soup2.find_all('p'):
            text_stat += text.text
        if bool(re.search(check, name, flags=re.I)) == True or bool(re.search(check, text_stat, flags=re.I)) == True: # or в тексте
            print(f'''Дата создания: {date}
Заголовок: "{name}"
Ссылка: {link}''')
            print()


print('Исполняется основное задание')
osnovnoe()
print('==================================================================')
print('Исполняется необязательная часть задания')
facultativcik()
