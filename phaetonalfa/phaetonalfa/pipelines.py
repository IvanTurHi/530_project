# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import datetime
#----------- День сегодня ----------
t2 = datetime.date.today()
t3 = datetime.timedelta(days=1)
time_I = (t2 - t3).strftime('%d.%m.%Y')

class PhaetonalfaPipeline(object):
    def process_item(self, item, spider):
        return item

class TestPip(object):
    def open_spider(self, spider):
        self.file = open('./phaetonalfa_data_today/flights_data.json', "w", encoding='utf-8')
        self.file1 = open('./phaetonalfa_data_today/days_before/'+ time_I +'.json', "w", encoding='utf-8')
        self.file_list = []

    def close_spider(self, spider):
        self.file.write(json.dumps(self.file_list, ensure_ascii=False))
        self.file.close()
        self.file1.write(json.dumps(self.file_list, ensure_ascii=False))
        self.file1.close()

    def process_item(self, item, spider):
        # self.file.write(str(dict(item)) + '\n\n')
        self.file_list.append(dict(item))
        return item
        
        # Scrapy crawl phaetonalfa