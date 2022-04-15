import scrapy
from scrapy1.items import Scrapy1Item
    

class TolmachSpider(scrapy.Spider):
    name = 'Tolmach'
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapy1.pipelines.TestPip': 400
        }
    }
    allowed_domains = ['tolmachevo.ru']
    start_urls = ['https://tolmachevo.ru/passengers/information/timetable//']
    
    def parse(self, response):
        def tweakFlight(listFlight):
            i=0
            while i < len(listFlight):
                if len(listFlight[i])==49:
                    listFlight.pop(i)
                i+=1
            for i in range(len(listFlight)):
                s1=listFlight[i][49:51]
                s2=listFlight[i][98:103]
                listFlight[i]=s1+s2
            return listFlight
        
        def tweakStatus(listStatus):
            for i in range(len(listStatus)):
                listStatus[i]=listStatus[i].strip()
            return listStatus
        
        item=Scrapy1Item()
        item['time']=response.xpath('/html/body/div[2]/div[3]/section/div/div/section/div/div/div[1]/div/div/article/div[1]/span[@class="tth-time-count"]/text()').extract()
        tempFlight=response.xpath('/html/body/div[2]/div[3]/section/div/div/section/div/div/div[1]/div/div/article/div[1]/span[1]/text()').extract()
        item['flight']=tweakFlight(tempFlight)
        tempStatus=response.xpath('/html/body/div[2]/div[3]/section/div/div/section/div/div/div[1]/div/div/article/div[1]/span[6]/text()').extract()
        item['status']=tweakStatus(tempStatus)
        item['url']=response.url
        yield item
        item2=Scrapy1Item()
        item2['time']=response.xpath('/html/body/div[2]/div[3]/section/div/div/section/div/div/div[2]/div/div/article/div[1]/span[@class="tth-time-count"]/text()').extract()
        tempFlight=response.xpath('/html/body/div[2]/div[3]/section/div/div/section/div/div/div[2]/div/div/article/div[1]/span[1]/text()').extract()
        item2['flight']=tweakFlight(tempFlight)
        tempStatus=response.xpath('/html/body/div[2]/div[3]/section/div/div/section/div/div/div[2]/div/div/article/div[1]/span[6]/text()').extract()
        item2['status']=tweakStatus(tempStatus)
        item2['url']=response.url
        yield item2

            
            
            
            