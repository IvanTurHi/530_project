import requests
import json
import datetime
from datetime import timedelta

path = 'https://www.svo.aero/bitrix/timetable/?direction=arrival&dateStart=2022-01-21T00:00:00%2B03:00&dateEnd=2022-01-22T00:00:00%2B03:00&perPage=9999&page=0&locale=ru'
tpat = 'https://www.svo.aero/bitrix/timetable/?direction=arrival&dateStart=2022-01-22T00:00:00%2B03:00&dateEnd=2022-01-23T00:00:00%2B03:00&perPage=99999&page=0&locale=ru'
path = 'https://www.svo.aero/bitrix/timetable/?direction=arrival&dateStart=2022-01-22T00:00:00%2B03:00&dateEnd=2022-01-23T00:00:00%2B03:00&perPage=9999&page=0&locale=ru'
path = 'https://www.svo.aero/bitrix/timetable/?direction=departure&dateStart=2022-01-22T00:00:00%2B03:00&dateEnd=2022-01-23T00:00:00%2B03:00&perPage=9999&page=0&locale=ru'
#
##re = requests.get('https://www.svo.aero/ru/timetable/arrival?date=today&period=allday&terminal=all')
#re = requests.get(path)
##print(re.text)
#
#file = open('help_js.json', 'w', encoding='utf-8')
#file.write(json.dumps(re.json(), ensure_ascii=False))
#
##file = open('help_js.json', 'r')
##k = json.loads('help_js.json')
##print(k)
##print(re.json())
#
#d = re.json()
#
#k = d['items'][0]
#
#for i in k:
#    print(i, k[i])

now = str(datetime.datetime.now())
tommorow = str(datetime.datetime.now() + timedelta(days=1))

path = 'sharik_links.txt'
with open(path) as f:
   lines = [line.rstrip() for line in f]
for i in range(len(lines)):
    start_date = lines[i].find('dateStart=')
    end_date = lines[i].find('dateEnd=')
    d_now = now.find(' ')
    d_tom = tommorow.find(' ')
    s = lines[i][:start_date+10] + now[:d_now] + lines[i][start_date+20:end_date+8] + tommorow[:d_tom] + lines[i][end_date+18:]
    lines[i] = s
