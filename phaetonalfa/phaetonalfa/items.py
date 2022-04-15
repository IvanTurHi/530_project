# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhaetonalfaItem(scrapy.Item):
    url = scrapy.Field()
    aircraft = scrapy.Field()
    origin = scrapy.Field()
    destination = scrapy.Field()
    direct_distance = scrapy.Field()
    coordinates = scrapy.Field()