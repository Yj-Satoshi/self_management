# -*- coding: utf-8 -*-
import re
import urllib.request
from bs4 import BeautifulSoup

address_choice = (
    {'no': 301, 'add_name': '宗谷地方'},
    {'no': 302, 'add_name': '上川・留萌地方'},
    {'no': 303, 'add_name': '網走・北見・紋別地方'},
    {'no': 304, 'add_name': '釧路・根室・十勝地方'},
    {'no': 305, 'add_name': '胆振・日高地方'},
    {'no': 306, 'add_name': '石狩・空知・後志地方'},
    {'no': 307, 'add_name': '渡島・檜山地方'},
    {'no': 308, 'add_name': '青森県'},
    {'no': 309, 'add_name': '秋田県'},
    {'no': 310, 'add_name': '岩手県'},
    {'no': 311, 'add_name': '山形県'},
    {'no': 312, 'add_name': '宮城県'},
    {'no': 313, 'add_name': '福島県'},
    {'no': 314, 'add_name': '茨城県'},
    {'no': 315, 'add_name': '群馬県'},
    {'no': 316, 'add_name': '栃木県'},
    {'no': 317, 'add_name': '埼玉県'},
    {'no': 318, 'add_name': '千葉県'},
    {'no': 319, 'add_name': '東京都'},
    {'no': 320, 'add_name': '神奈川県'},
    {'no': 321, 'add_name': '山梨県'},
    {'no': 322, 'add_name': '長野県'},
    {'no': 323, 'add_name': '新潟県'},
    {'no': 324, 'add_name': '富山県'},
    {'no': 325, 'add_name': '石川県'},
    {'no': 326, 'add_name': '福井県'},
    {'no': 327, 'add_name': '静岡県'},
    {'no': 328, 'add_name': '岐阜県'},
    {'no': 329, 'add_name': '愛知県'},
    {'no': 330, 'add_name': '三重県'},
    {'no': 331, 'add_name': '大阪府'},
    {'no': 332, 'add_name': '兵庫県'},
    {'no': 333, 'add_name': '京都府'},
    {'no': 334, 'add_name': '滋賀県'},
    {'no': 335, 'add_name': '奈良県'},
    {'no': 336, 'add_name': '和歌山県'},
    {'no': 337, 'add_name': '島根県'},
    {'no': 338, 'add_name': '広島県'},
    {'no': 339, 'add_name': '鳥取県'},
    {'no': 340, 'add_name': '岡山県'},
    {'no': 341, 'add_name': '香川県'},
    {'no': 342, 'add_name': '愛媛県'},
    {'no': 343, 'add_name': '徳島県'},
    {'no': 344, 'add_name': '高知県'},
    {'no': 345, 'add_name': '山口県'},
    {'no': 346, 'add_name': '福岡県'},
    {'no': 347, 'add_name': '佐賀県'},
    {'no': 348, 'add_name': '長崎県'},
    {'no': 349, 'add_name': '熊本県'},
    {'no': 350, 'add_name': '大分県'},
    {'no': 351, 'add_name': '宮崎県'},
    {'no': 352, 'add_name': '鹿児島県'},
    {'no': 353, 'add_name': '沖縄本島地方'},
    {'no': 354, 'add_name': '大東島地方'},
    {'no': 355, 'add_name': '宮古島地方'},
    {'no': 356, 'add_name': '八重山地方'},
)

address = '大阪府'
for a in address_choice:
    if a['add_name'] == address:
        address_key = (a['no'])

url_add = 'https://www.jma.go.jp/jp/week/' + str(address_key) + '.html'
url = urllib.request.urlopen(url_add)
soup = BeautifulSoup(url, 'lxml')

city = soup.find("th", {"class": "cityname"}).text
days = soup.find("table", {"id": "infotablefont"}).find_all("tr")[0].find_all("th")
max_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[4].find_all("td")
min_temp = soup.find("table", {"id": "infotablefont"}).find_all("tr")[5].find_all("td")

weather = []

daylist = []
weeklist = []
for day in days:
    day = day.text

    if '日付' not in day:
        weeklist.append(day[-1])
        daylist.append(day[:-1])

maxtemplist = []
for maxtemp in max_temp:
    maxtemp = maxtemp.text

    if '最高' not in maxtemp:
        maxtemp = maxtemp.replace('\n', '').replace('\t', '').replace('(', '{').replace(')', '}')
        maxtemp = re.sub('{.*?}', '', maxtemp)

        if '／' in maxtemp:
            maxtemp = None
        else:
            maxtemp = int(maxtemp)

        maxtemplist.append(maxtemp)

mintemplist = []
for mintemp in min_temp:
    mintemp = mintemp.text

    if '最低' not in mintemp:
        mintemp = mintemp.replace('\n', '').replace('\t', '').replace('(', '{').replace(')', '}')
        mintemp = re.sub('{.*?}', '', mintemp)

        if '／' in mintemp:
            mintemp = None
        else:
            mintemp = int(mintemp)

        mintemplist.append(mintemp)

weather.append(city)
weather.append(weeklist)
weather.append(daylist)
weather.append(maxtemplist)
weather.append(mintemplist)

print(weather)
