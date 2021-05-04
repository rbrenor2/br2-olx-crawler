# -*- coding: utf-8 -*-
import scrapy
from ..items import IphoneOfferItem
from datetime import datetime, timedelta


class IphoneoffersSpider(scrapy.Spider):
    name = 'iphoneoffers'
    allowed_domains = ['http://www.olx.com.br/', 'www.olx.com.br']
    start_urls = ['http://www.olx.com.br/celulares/iphone/usado?q=iphone/']

    def parse(self, response):
        offerItem = IphoneOfferItem()
        offerList = response.xpath("//ul[@class='sc-1fcmfeb-1 kntIvV']/li")
        
        for offer in offerList: 
            offerItem["product_id"] = offer.xpath("a[@class='fnmrjs-0 fyjObc']/@data-lurker_list_id").get()
            offerItem["url"] = offer.xpath('a[@class="fnmrjs-0 fyjObc"]/@href').get()
            offerItem["title"] = offer.xpath("a[@class='fnmrjs-0 fyjObc']/@title").get()
            offerItem["price"] = offer.xpath("a[@class='fnmrjs-0 fyjObc']//span[@class='sc-ifAKCX eoKYee']/text()").get()
            offerItem["post_time"] = offer.xpath("a[@class='fnmrjs-0 fyjObc']//p[@class='sc-1iuc9a2-4 hDBjae sc-ifAKCX fWUyFm']/text()").get()
            offerItem["city"] = offer.xpath("a[@class='fnmrjs-0 fyjObc']//span[@class='sc-7l84qu-1 ciykCV sc-ifAKCX dpURtf']/@title").get()
            offerItem["thumb_url"] = offer.xpath("a[@class='fnmrjs-0 fyjObc']//div[@class='fnmrjs-1 gIEtsI']//img/@src").get()
            offerItem["is_featured"] = offer.xpath('a[@class="fnmrjs-0 fyjObc"]/@data-lurker_is_featured').get()
            offerItem["list_position"] = offer.xpath('a[@class="fnmrjs-0 fyjObc"]/@data-lurker_list_position').get()

            yield offerItem

        nextPageUrl = response.xpath(""".//a[@data-lurker-detail='next_page']/@href""").get()
        if nextPageUrl is not '' and nextPageUrl is not None:
            if 'o=' in nextPageUrl:
                pageNum = nextPageUrl.split('o=')[1].split('&')[0]
                print(f'Current page: {pageNum}')
            else:
                print(f'Current page: 1')
            yield response.follow(url=nextPageUrl, callback=self.parse)   


    

    

