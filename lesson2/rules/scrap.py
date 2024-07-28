import random
from asyncio import sleep

import requests
from bs4 import BeautifulSoup
import json
import csv

# url = 'https://likumi.lv/ta/id/274865'
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open("index.html", "w", encoding="utf-8") as f:
#     f.write(src)

pant_numbers = [
    ['1', '2', '3', '4', '5', '6'],
    ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'],
    ['25', '25.1'],
    ['26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'],
    ['39', '40', '41', '42', '43'],
    ['44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56'],
    ['57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82'],
    ['83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98'],
    ['99', '100', '101', '102', '103', '104', '105', '106'],
    ['107', '108', '109', '110', '111', '112', '113'],
    ['114', '115', '116', '117', '118', '119', '120', '121', '122', '123'],
    ['124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138'],
    ['139', '140', '141', '142', '143', '144'],
    ['145', '146', '147', '148', '149', '150', '151'],
    ['152', '153', '154', '155', '156', '157', '158', '159'],
    ['159.1', '159.2', '159.3'],
    ['160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171'],
    ['172', '173', '174', '175'],
    ['176', '177', '178', '179', '180', '181', '182'],
    ['183', '184', '185', '186', '187', '188', '189'],
    ['190', '191', '192', '193', '194', '195'],
    ['196', '197', '198', '199'],
    ['200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212'],
    ['212.1', '212.2', '212.3', '212.4', '212.5', '212.6', '212.7'],
    ['213', '214', '215', '216', '217'],
    ['218', '219', '220', '221', '222', '223', '224', '225', '226'],
    ['227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246'],
    ['247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288'],
    ['289', '290', '291', '292', '293', '294', '295', '296'],
    ['297', '298', '299'],
    ['297', '298', '299'],
    ['297', '298', '299'],
    ['297', '298', '299'],
    ['297', '298', '299'],
    ['297', '298', '299'],
    ['297', '298', '299']

]

# def filter_pants(item, iterator):
#     return list(filter(filter_first, pants))


def filter_first(item):
    if item['data-num'] in pant_numbers[p]:
        return True
    else:
        return False


def has_att_data_num(tag):
    return tag.has_attr('data-num')


with open("index.html", encoding="utf-8") as f:
    src = f.read()

soup = BeautifulSoup(src, "lxml")
all_213_divs = soup.find_all('div', class_='TV213')

first = ['1', '2', '3', '4', '5', '6']


all_pants_li = soup.find('ul', class_='doc-saturs-ul').children
# print(all_pants_li[1])
app_pants_names = []
for item in all_pants_li:
    text = item.find('div').text
    app_pants_names.append(text)

# print(app_pants_names)

p = 0
check = 0

for pant_name in app_pants_names:

    pants = soup.find_all(has_att_data_num)
    correct_pants = list(filter(filter_first, pants))
    pants = []
    for item in correct_pants:
        number = item['data-num']
        print(item)
        text = item.find('p', class_='TVP').text
        all_subpoints = item.find_all('p', class_='limenis2')
        subpoints = []
        iterator = 1
        for sub_item in all_subpoints:
            sub_num = number + "." + str(iterator)
            sub_text = sub_item.text
            subpoints.append(
                {
                    'number': sub_num,
                    'text': sub_text,
                    'terms': [],
                    'img': [],
                    'references': [],
                    'source': []
                }
            )
            iterator += 1
        pants.append(
            {
                'number': number,
                'text': text,
                'references': [],
                'terms': [],
                'subpoints': subpoints,
                'img': [],
                'source': [],
                'brief_item_desc': ''
            }
        )
        check += 1

    with open(f'data/{pant_name}.json', 'w', encoding='utf-8') as f:
        json.dump(pants, f, ensure_ascii=False, indent=4)
    p += 1
print(check)
