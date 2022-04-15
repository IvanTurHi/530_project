# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapy1Pipeline:
    def process_item(self, item, spider):
        return item
    
class TestPip(object):
    def open_spider(self, spider):
        # from datetime import date
        # current_date = date.today()
        # date_time = current_date.strftime("%d_%m_%Y")
        # f='./'+date_time+'_Tolmachevo_today.json'
        self.file = open(r'../phaeton/phaeton_data_today/today.json', "r", encoding='utf-8')
        self.file_list = json.load(self.file)
        self.file.close()
        self.file = open(r'../phaeton/phaeton_data_today/today.json', "w", encoding='utf-8')

    def close_spider(self, spider):
        
        self.file.write(json.dumps(self.file_list, ensure_ascii=False))
        self.file.close()

    def process_item(self, item, spider):
        self.file_list.append(dict(item))
        return item