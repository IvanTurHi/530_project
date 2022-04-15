# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json

class SharikPipeline:
    def process_item(self, item, spider):
        return item

class TestPip(object):
    def open_spider(self, spider):
        self.file = open(r'../phaeton/phaeton_data_today/today.json', "r", encoding='utf-8')
        self.file_list = json.load(self.file)
        self.file.close()
        self.file = open(r'../phaeton/phaeton_data_today/today.json', "w", encoding='utf-8')

    def close_spider(self, spider):
        self.file.write(json.dumps(self.file_list, ensure_ascii=False))
        self.file.close()

    def process_item(self, item, spider):
        # self.file.write(str(dict(item)) + '\n\n')
        self.file_list.append(dict(item))
        return item

# Scrapy crawl sheremet