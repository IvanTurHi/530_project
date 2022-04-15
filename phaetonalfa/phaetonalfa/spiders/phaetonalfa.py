import json
import logging
from urllib.parse import urljoin
import scrapy
import os
from phaetonalfa.items import PhaetonalfaItem
import datetime
 
 
class phaetonalfaSpider(scrapy.Spider):
    name = 'phaetonalfa'
    #allowed_domains = ['ru.flightaware.com']
    #start_urls = ['https://ru.flightaware.com/live/flight/KLM2906']
    custom_settings = {
        'ITEM_PIPELINES': {
            'phaetonalfa.pipelines.TestPip': 400
        }
    }
    
    def start_requests(self):
        path = os.path.realpath('fligth_links_today.txt')
        logging.debug("path:" + str(path))
        with open(path, encoding="utf8") as f:
            lines = [line.rstrip() for line in f]
        for url in lines:
                yield scrapy.Request(url,
                                     callback=self.parse) 
                                     
    def parse(self, response):

        data = json.loads(response.xpath('//script[contains(text(), \'var trackpollBootstrap = {\')]/text()').re(
            'var trackpollBootstrap = (\{.+\})')[0])
        data = next(iter(data["flights"].values()))
        
        phaetonalfaitem = PhaetonalfaItem()
        phaetonalfaitem['url'] = response.url
        aircraft = data['aircraft']['friendlyType']
        logging.debug(aircraft)
        #yield {'aircraft': aircraft}
        phaetonalfaitem['aircraft'] = aircraft
 
        origin = data['origin']['altIdent']
        logging.debug(origin)
        #yield {'origin': origin}
        phaetonalfaitem['origin'] = origin
 
        destination = data['destination']['altIdent']
        logging.debug(destination)
        #yield {'destination': destination}
        phaetonalfaitem['destination'] = destination
 
        direct_distance = data['flightPlan']['directDistance']
        logging.debug(direct_distance)
        #yield {'direct_distance': direct_distance}
        phaetonalfaitem['direct_distance'] = direct_distance
 
        for flight in data['activityLog']['flights']:
            if flight['flightStatus'] == 'arrived':
                track_log = flight['links']['trackLog']
                yield scrapy.Request(urljoin(response.url, track_log),
                                     callback = self.parse_log,
                                     meta = {'items': phaetonalfaitem})
                #yield scrapy.Request("https://ru.flightaware.com/live/flight/JAL44/history/20220304/1900Z/EGLL/RJTT/tracklog",
                #                    callback = self.parse_log,
                #                    meta = {'items': phaetonalfaitem})
                break


    def parse_log(self, response):
        logging.debug(response.url)
        phaetonalfaitem = response.meta['items']
        coordinates = response.xpath(".//span[@class='show-for-medium-up']/text()").extract()
        phaetonalfaitem['coordinates'] = coordinates
        yield phaetonalfaitem

        #Scrapy crawl phaetonalfa
