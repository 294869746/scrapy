# -*- coding: utf-8 -*-
import scrapy
import os
import requests

from picture.items import PictureItem


class ExampleSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['qq.yh31.com']
    start_urls = ['http://qq.yh31.com/zjbq/0634513.html']
    base_url = 'http://qq.yh31.com'

    def parse(self, response, ):
        # print(response.body)
        base_url = 'http://qq.yh31.com'
        item = PictureItem()

        for i in range(1,len(response.xpath('//img[@class="restrictImg"]'))):
            if not os.path.exists('mypic'):
                os.makedirs('mypic')
            item['img_url'] = base_url+response.xpath('//img[@class="restrictImg"]/@src').extract()[i]
            print(item['img_url'])
            r = requests.get(item['img_url'])
            filename = 'mypic/{}.gif'.format(i)
            with open(filename,'w') as f:
                f.write(r.content)
        # data = response.xpath('img[@class="restrictImg"]')
        # filename = "/home/zhouchangjian/Desktop/picture/picture/shuju"
        # with open(filename,'w') as f:
        #     f.write(response.body)
        # #     for da in data:
        # #         f.writelines(da)
        # #         print(da)
        # i = 0
        # for content in response.xpath('img[@class="restrictImg"]'):
        #     i =+ 1
        #     content = response.xpath('img[@class="restrictImg"]')[i];
        #     item = PictureItem()
        yield item