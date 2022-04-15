import scrapy
import logging
import os
from .. items import SharikItem
import datetime
from datetime import timedelta

class SheremetSpider(scrapy.Spider):
    name = 'sheremet'
    custom_settings = {
        'ITEM_PIPELINES': {
            'sharik.pipelines.TestPip': 400
        }
    }

    def start_requests(self):
        path = os.path.realpath('sharik_links.txt')
        logging.debug("path:" + str(path))
        now = str(datetime.datetime.now())
        tommorow = str(datetime.datetime.now() + timedelta(days=1))
        with open(path) as f:
            lines = [line.rstrip() for line in f]

        # сайт шереметьево просто так не получится распарсить из-за JS, поэтому посылаем запрос именно на данные и парсим его
        # ниже код для составления запроса в зависимости от даты
        for i in range(len(lines)):
            start_date = lines[i].find('dateStart=')
            end_date = lines[i].find('dateEnd=')
            d_now = now.find(' ')
            d_tom = tommorow.find(' ')
            s = lines[i][:start_date + 10] + now[:d_now] + lines[i][start_date + 20:end_date + 8] + tommorow[:d_tom] + \
                lines[i][end_date + 18:]
            lines[i] = s
        for url in lines:
                yield scrapy.Request(url,
                                     callback=self.parse)

    def parse(self, response):
        js_r = response.json()
        js_r_i = js_r['items']
        time_list = []
        flight_list = []
        status_list = []

        for i in range(len(js_r_i)):
            n_flight = js_r['items'][i]
            time_s = n_flight['t_st']
            time = time_s[time_s.find('T')+1:time_s.find('T')+6]
            flight_code = n_flight['co']['code']
            flight_num = n_flight['flt']
            flight = flight_code+' '+flight_num
            status = n_flight['vip_status_rus']
            if 'departure' in response.url:
                url = 'https://www.svo.aero/ru/timetable/departure?date=today&period=allday&terminal=all'
            else:
                url = 'https://www.svo.aero/ru/timetable/arrival?date=today&period=allday&terminal=all'

            time_list.append(time)
            flight_list.append(flight)
            status_list.append(status)

        sharikitem = SharikItem()
        sharikitem['time'] = time_list
        sharikitem['flight'] = flight_list
        sharikitem['status'] = status_list
        sharikitem['url'] = url

        yield sharikitem

        #Запускать в конце суток, так можно отследить статус рейсов




