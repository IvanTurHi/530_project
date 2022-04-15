import scrapy
import logging
import os
from .. items import PhaetonItem


class phaetonSpyder(scrapy.Spider):
    name = 'phaeton'
    custom_settings = {
        'ITEM_PIPELINES': {
            'phaeton.pipelines.TestPip': 400
        }
    }

    def start_requests(self):
        path = os.path.realpath('phaeton_links.txt')
        logging.debug("path:" + str(path))
        with open(path) as f:
            lines = [line.rstrip() for line in f]
        for url in lines:
                yield scrapy.Request(url,
                                     callback=self.parse)

    def parse(self, response):

        def get_time():
            logging.debug("url test:" + str(response.url))
            flight_time = response.xpath("//div[@data-ti='time']").getall()
            for i in range(0, len(flight_time)):
                flight_time[i] = flight_time[i][len(flight_time[i]) - 18:len(flight_time[i]) - 13]
            return flight_time

        def get_flight():
            logging.debug("url test:" + str(response.url))
            flight_name = response.xpath("//div[@data-ti='flight_number']//text()").getall()
            clear_flight_name = []
            for i in range(1, len(flight_name), 2):
                clear_flight_name.append(flight_name[i].rstrip())
            return clear_flight_name

        def get_status():
            logging.debug("url test:" + str(response.url))

            flight_status = response.xpath("//div[@data-ti='status']//text()").getall()
            i = 0
            while i < len(flight_status):
               flight_status[i] = flight_status[i].strip()
               k = flight_status[i].find("xa0")
               if k != -1:
                   flight_status[i] = flight_status[i][:k-1] + flight_status[i][k+3:]
               i = i + 1

            return flight_status

        #=====================================================

        phaetonitem = PhaetonItem()
        phaetonitem['time'] = get_time()
        phaetonitem['flight'] = get_flight()
        phaetonitem['status'] = get_status()
        phaetonitem['url'] = response.url
        yield phaetonitem

        #=====================================================
