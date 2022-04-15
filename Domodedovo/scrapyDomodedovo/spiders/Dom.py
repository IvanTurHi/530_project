import scrapy
from scrapyDomodedovo.items import ScrapydomodedovoItem
import pandas as pd

class DomSpider(scrapy.Spider):
    name = 'Dom'
    custom_settings = {
        'ITEM_PIPELINES': {
            'scrapyDomodedovo.pipelines.NormSaving': 400
        }
    }
    allowed_domains = ['www.dme.ru']
    start_urls = ['https://www.dme.ru/book/live-board/?searchText=&column=4&sort=1&start=0&end=1500&direction=A&page=1&count=&isSlider=1']
    curr='https://www.dme.ru/Ru/autogenerated/Flight/OnlineTableWideScrolling?searchText=&column=4&sort=1&start=0&end=1500&direction=A&isSlider=1&page=1'
    curr2='https://www.dme.ru/Ru/autogenerated/Flight/OnlineTableWideScrolling?searchText=&column=4&sort=1&start=0&end=1500&direction=D&isSlider=1&page=1'
    newd='https://www.dme.ru/book/live-board/?searchText=&column=4&sort=1&start=0&end=1500&direction=D&page=1&count=&isSlider=1'
    FlagDirection=False
    def fillItem(self, neededTable):
        item=ScrapydomodedovoItem()
        name1=neededTable.columns[2]
        name2=neededTable.columns[3]
        name3=neededTable.columns[5]
        templistT=neededTable[name1].to_list()
        for i in range(len(templistT)):
            if templistT[i]!=templistT[i]:
                templistT[i]='0'
            else:
                templistT[i]=templistT[i][7:]
        item['time']=templistT
        item['flight']=neededTable[name2].to_list()
        templistS=neededTable[name3].to_list()
        for i in range(len(templistS)):
            if templistS[i]!=templistS[i]:
                templistS[i]='0'
            else:
                mean_index = len(templistS[i]) // 2
                templistS[i]=templistS[i][:mean_index]
        item['status']=templistS
        if self.FlagDirection==False:
            item['url']='https://www.dme.ru/book/live-board/?searchText=&column=4&sort=1&start=0&end=1500&direction=A&page=1&count=&isSlider=1'
        else:
             item['url']=self.newd
        return item
    
    def parse(self, response):  
        item=ScrapydomodedovoItem()
        tables = pd.read_html(response.url) 
        neededTable = tables[2]
        neededTable.columns = [tup[1] if tup[1] else tup[0] for tup in neededTable.columns]
        item=self.fillItem(neededTable)
        yield item
        npage=int(self.curr[-1])
        npage+=1
        self.curr=self.curr[:-1]
        self.curr+=str(npage)
        print(self.curr)
        yield scrapy.Request(self.curr,method='POST',callback=self.parseN)
        
    def parseN(self, response):
        if response.body.decode("utf-8").strip()=='':
            if self.FlagDirection==False:
                self.curr=self.curr2
                self.FlagDirection=True
                self.curr=self.curr[:-1]
                self.curr+='1'
                yield scrapy.Request(self.newd,callback=self.parse)
                return
            else:
                return
        newhtml='<table>'+response.body.decode("utf-8")+'</table>'
        tables = pd.read_html(newhtml)
        neededTable = tables[0]
        item=ScrapydomodedovoItem()
        item=self.fillItem(neededTable)
        yield item
        npage=int(self.curr[-1])
        npage+=1
        self.curr=self.curr[:-1]
        self.curr+=str(npage)
        yield scrapy.Request(self.curr,method='POST',callback=self.parseN)
       

            