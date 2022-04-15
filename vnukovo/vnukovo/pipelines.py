# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class VnukovoPipeline:
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
        item_dep = {}
        item_dep['time'] = item['time']
        item_dep['flight'] = item['flight']
        item_dep['status'] = item['status']
        item_dep['url'] = item['url']
        item_arr = {}
        item_arr['time'] = item['a_time']
        item_arr['flight'] = item['a_flight']
        item_arr['status'] = item['a_status']
        item_arr['url'] = item['a_url']
        self.file_list.append(dict(item_dep))
        self.file_list.append(dict(item_arr))
        return item

# Scrapy crawl vnuk