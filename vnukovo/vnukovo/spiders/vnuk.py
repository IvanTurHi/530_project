import scrapy
import os
import logging
from .. items import VnukovoItem

class VnukSpider(scrapy.Spider):
    name = 'vnuk'
    custom_settings = {
        'ITEM_PIPELINES': {
            'vnukovo.pipelines.TestPip': 400
        }
    }

    def start_requests(self):
        path = os.path.realpath('vnukovo_links.txt')
        logging.debug("path:" + str(path))
        with open(path) as f:
            lines = [line.rstrip() for line in f]
        k = 3
        for url in lines:
            k += 1
            yield scrapy.Request(url,
                                 callback=self.parse)


    def parse(self, response):


        departure_flight_list = response.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div[4]/table/tbody/tr[*]/td[2]/a/text()').getall()
        departure_time_list = response.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div[4]/table/tbody/tr[*]/td[1]/text()').getall()
        departure_status_list = response.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div[4]/table/tbody/tr[*]/td[6]/text()').getall()


        arrival_flight_list = response.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div[5]/table/tbody/tr[*]/td[2]/a/text()').getall()
        arrival_time_list = response.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div[5]/table/tbody/tr[*]/td[1]/text()').getall()
        arrival_status_list = response.xpath('/html/body/div[2]/div[2]/div[3]/div[4]/div[5]/table/tbody/tr[*]/td[6]/text()').getall()


        vnukovoitem = VnukovoItem()
        vnukovoitem['time'] = departure_time_list
        vnukovoitem['flight'] = departure_flight_list
        vnukovoitem['status'] = departure_status_list
        vnukovoitem['url'] = 'http://www.vnukovo.ru/flights/online-timetable/#tab-sortie'


        vnukovoitem['a_time'] = arrival_time_list
        vnukovoitem['a_flight'] = arrival_flight_list
        vnukovoitem['a_status'] = arrival_status_list
        vnukovoitem['a_url'] = 'http://www.vnukovo.ru/flights/online-timetable/#tab-arrivals'
        yield vnukovoitem
