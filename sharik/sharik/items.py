# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SharikItem(scrapy.Item):
    time = scrapy.Field()
    flight = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()
