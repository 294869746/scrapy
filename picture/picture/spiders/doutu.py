# -*- coding: utf-8 -*-
import os
import scrapy
import requests
from picture.items import DoutuItems
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Doutu(scrapy.Spider):
    name = "doutu"
    allowed_domains = ["doutula.com", "sinaimg.cn"]
    start_urls = ['https://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1,40)] # 我们暂且爬取40页图片

    def parse(self, response):
        i = -1
        for content in response.xpath('//a[@class="col-xs-6 col-sm-3"]'):
            i += 1
            content = response.xpath('//a[@class="col-xs-6 col-sm-3"]')[i]
            item = DoutuItems()
            item['img_url'] = content.xpath('//img/@data-original').extract()[i]
            print("********************************")
            print(item['img_url'])
            print(content)
            print(content.xpath('//img/@data-original')[i])
            print("********************************")
            item['name'] = content.xpath('//p/text()').extract()[i]
            # try:
            #     if not os.path.exists('doutu'):
            #         os.makedirs('doutu')
            #     r = requests.get(item['img_url'])
            #     filename = 'doutu/{}'.format(item['name']) + item['img_url'][-3:]
            #     with open(filename, 'w') as fo:
            #         fo.write(r.content)
            # except:
            #     print('Error')
        yield item