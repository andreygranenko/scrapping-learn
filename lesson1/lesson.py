import re

from bs4 import BeautifulSoup

with open("blank/index.html", encoding="utf-8") as f:
    src = f.read()

# print(src)
soup = BeautifulSoup(src, "lxml")
title = soup.title
# print(title.text)
# print(title.string)

all_h1 = soup.find_all('h1')
# print(all_h1)

user_info = soup.find(class_='user__name').text.strip()
# print(user_info)

user_name = soup.find('div', {'class': "user__name"}).text.strip()
user_birth_date = soup.find('div', {'class': "user__birth__date"}).find_all('span')[1].text
user_city= soup.find('div', {'class': "user__city"}).find_all('span')[1].text
print("user city " + user_city + " user name " + user_name + " user birth date " + user_birth_date)


all_a = soup.find_all('a')
for item in all_a:
    item_text = item.text.strip()
    item_url = item.get('href')
    print(item_text)
    print(item_url)

find_by_text = soup.find('span', string=re.compile('Город:'))
print(find_by_text)

all_cities = soup.find_all('span', string=re.compile("([Гг]ород)"))
print(all_cities)