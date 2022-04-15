# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VnukovoItem(scrapy.Item):
    time = scrapy.Field()
    flight = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()
    a_time = scrapy.Field()
    a_flight = scrapy.Field()
    a_status = scrapy.Field()
    a_url = scrapy.Field()
