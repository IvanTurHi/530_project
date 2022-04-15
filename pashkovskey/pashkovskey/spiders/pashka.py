import scrapy
import os
import logging
from .. items import PashkovskeyItem
import time
from random import choice


class PashkaSpider(scrapy.Spider):
    name = 'pashka'
    custom_settings = {
        'ITEM_PIPELINES': {
            'pashkovskey.pipelines.TestPip': 400
        }
    }

    def start_requests(self):
        path = os.path.realpath('pashkovskey_links.txt')
        logging.debug("path:" + str(path))

        desktop_agents = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

        def random_headers():
            return {'User-Agent': choice(desktop_agents),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

        with open(path) as f:
            lines = [line.rstrip() for line in f]
        for url in lines:
                yield scrapy.Request(url, headers=random_headers(),
                                     callback=self.parse)

    def parse(self, response):

        time_list = response.xpath('//*[@id="root"]/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div[7]/div/table/tbody[*]/tr[1]/td[1]/text()').getall()

        total = len(time_list)

        flight_list = []
        status_list = []
        time_list = []

        for i in range(1, total):
            prefix = response.xpath('//*[@id="root"]/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div[7]/div/table/tbody[{}]/tr[1]/td[4]/a/text()[1]'.format(i)).get()

            if prefix == None:
                prefix = response.xpath('//*[@id="root"]/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div[7]/div/table/tbody[{}]/tr[1]/td[4]/text()[1]'.format(i)).get()


            num_code = response.xpath('//*[@id="root"]/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div[7]/div/table/tbody[{}]/tr[1]/td[4]/a/span[1]/text()'.format(i)).get()

            if num_code == None:
                num_code = response.xpath('//*[@id="root"]/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div[7]/div/table/tbody[{}]/tr[1]/td[4]/span[1]/text()'.format(i)).get()

            flight_list.append(prefix + ' ' + num_code)

            status_list.append(response.xpath('//*[@id="root"]/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div[7]/div/table/tbody[{}]/tr[1]/td[5]/div[1]/text()'.format(i)).get())
            stats = response.xpath('//*[@id="root"]/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div[7]/div/table/tbody[{}]/tr[2]/td/text()'.format(i)).get()
            if stats == 'Отменен':
                status_list[i-1] = stats

            time_list.append(response.xpath('//*[@id="root"]/div/div[2]/main/div/div[2]/div/div[1]/div[1]/div[7]/div/table/tbody[{}]/tr[1]/td[1]/text()'.format(i)).get())



        pashkaitem = PashkovskeyItem()
        pashkaitem['time'] = time_list
        pashkaitem['flight'] = flight_list
        pashkaitem['status'] = status_list
        pashkaitem['url'] = response.url
        time.sleep(180)
        yield pashkaitem