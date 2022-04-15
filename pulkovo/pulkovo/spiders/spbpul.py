import scrapy
import os
import logging
from .. items import PulkovoItem


class SpbpulSpider(scrapy.Spider):
    name = 'spbpul'
    custom_settings = {
        'ITEM_PIPELINES': {
            'pulkovo.pipelines.TestPip': 400
        }
    }

    def start_requests(self):
        path = os.path.realpath('pulkovo_links.txt')
        logging.debug("path:" + str(path))
        with open(path) as f:
            lines = [line.rstrip() for line in f]
        for url in lines:
                yield scrapy.Request(url,
                                     callback=self.parse)

    def parse(self, response):
        js_b = response.json()
        time_list = []
        flight_list = []
        status_list = []
        pulkovoitem = PulkovoItem()

        if 'departure' in response.url:

            for i in range(len(js_b)):
                #print(js_b[i]['OD_STD'][11:16], js_b[i]['OD_FLIGHT_NUMBER'], js_b[i]['OD_STATUS_RU'])
                time_list.append(js_b[i]['OD_STD'][11:16])
                flight_list.append(js_b[i]['OD_FLIGHT_NUMBER'])
                status_list.append(js_b[i]['OD_STATUS_RU'])

            pulkovoitem['time'] = time_list
            pulkovoitem['flight'] = flight_list
            pulkovoitem['status'] = status_list
            pulkovoitem['url'] = 'https://pulkovoairport.ru/passengers/departure/?when=0'

        else:

            for i in range(len(js_b)):
                # print(js_b[i]['OD_STD'][11:16], js_b[i]['OD_FLIGHT_NUMBER'], js_b[i]['OD_STATUS_RU'])
                time_list.append(js_b[i]['OA_STA'][11:16])
                flight_list.append(js_b[i]['OA_FLIGHT_NUMBER'])
                status_list.append(js_b[i]['OA_STATUS_RU'])

            pulkovoitem['time'] = time_list
            pulkovoitem['flight'] = flight_list
            pulkovoitem['status'] = status_list
            pulkovoitem['url'] = 'https://pulkovoairport.ru/passengers/arrival/?when=0'


        yield pulkovoitem
