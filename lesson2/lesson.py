import random
from asyncio import sleep

import requests
from bs4 import BeautifulSoup
import json
import csv
#
# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

}
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)
#
# # with open("index.html", "w", encoding="utf-8") as f:
#     # f.write(src)
#
# with open('index.html', encoding='utf-8') as f:
#     src = f.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
#
# all_categories_dict = {}
#
# for item in all_products_hrefs:
#     item_href = "https://health-diet.ru" + item.get('href')
#     item_text = item.text
#     # print(f'{item_text}: {item_href}')
#     all_categories_dict[item_text] = item_href
#
# with open('all_categories_dict.json', 'w', encoding='utf-8') as f:
#     json.dump(all_categories_dict, f, indent=4, ensure_ascii=False)

with open('all_categories_dict.json', encoding='utf-8') as f:
    all_categories = json.load(f)

# print(all_categories)
iteration_count = int(len(all_categories)) - 1
count = 0
for category_name, category_href in all_categories.items():

    rep = [',', ' ', '-', "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f'data/{count}_{category_name}.html', 'w', encoding='utf-8') as f:
        f.write(src)

    with open(f'data/{count}_{category_name}.html', encoding='utf-8') as f:
        src = f.read()

    soup = BeautifulSoup(src, 'lxml')

    # page check on table presence

    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue

    all_th = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
    print(all_th)
    product = all_th[0].text
    calories = all_th[1].text
    protein = all_th[2].text
    fat = all_th[3].text
    carbs = all_th[4].text

    with open(f"data/{count}_{category_name}.csv", "w", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(
            (
                product,
                calories,
                protein,
                fat,
                carbs
            )
        )

    all_tr = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
    product_info = []
    for item in all_tr:
        products_tds = item.find_all('td')

        title = products_tds[0].text
        calories = products_tds[1].text
        protein = products_tds[2].text
        fat = products_tds[3].text
        carbs = products_tds[4].text

        product_info.append(
            {
                'Title': title,
                'Calories': calories,
                'Protein': protein,
                'Fat': fat,
                'Carbs': carbs
            }
        )

        with open(f"data/{count}_{category_name}.csv", "a", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(
                (
                    title,
                    calories,
                    protein,
                    fat,
                    carbs
                )
            )

    with open(f"data/{count}_{category_name}.json", "w", encoding='utf-8') as f:
        json.dump(product_info, f, ensure_ascii=False, indent=4)

    count += 1
    print(f'#iteration {count} {category_name} written ...')
    iteration_count -= 1

    if iteration_count == 0:
        print('work is over')
        break

    print(f"iteration remain {iteration_count}")
    sleep(random.randrange(2, 4))