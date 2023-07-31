# -*- coding: utf-8 -*-
import scrapy
from ..items import IphoneOfferItem
from datetime import datetime, timedelta


class IphoneoffersSpider(scrapy.Spider):
    name = 'iphoneoffers'
    allowed_domains = ['www.olx.com.br']
    start_urls = ['https://www.olx.com.br/celulares/apple?q=iphone']

    def parse(self, response):
        offerItem = IphoneOfferItem()
        offerList = response.xpath('//ul[@id="ad-list"]/li//a[@data-ds-component="DS-Link"]')
    
        for offer in offerList: 
            print(offer)
            offerItem["product_id"] = offer.xpath('/@data-lurker_list_id').get()
            offerItem["url"] = offer.xpath('/@href').get()
            offerItem["title"] = offer.xpath('/@title').get()
            offerItem["price"] = offer.xpath('//span[starts-with(@aria-label,"Preço do")]/text()').get()
            offerItem["post_time"] = offer.xpath('//span[starts-with(@aria-label,"Anúncio publicado em")]/text()').get()
            offerItem["city"] = offer.xpath('//span[starts-with(@aria-label,"Localização:")]/text()').get()
            offerItem["thumb_url"] =  offer.xpath('//img[starts-with(@alt,"Título do a")]/@src').get()
            offerItem["is_featured"] = offer.xpath('//@data-lurker_is_featured').get()
            offerItem["list_position"] = offer.xpath('//@data-lurker_list_position').get()
            offerItem["scrap_time"] = datetime.now().strftime("%Y-%m-%d %H:%M")

            yield offerItem

        nextPageUrl = response.xpath(""".//a[@data-lurker-detail='next_page']/@href""").get()
        if nextPageUrl is not '' and nextPageUrl is not None:
            if 'o=' in nextPageUrl:
                pageNum = nextPageUrl.split('o=')[1].split('&')[0]
                print(f'Current page: {pageNum}')
            else:
                print(f'Current page: 1')
            yield response.follow(url=nextPageUrl, callback=self.parse)   


    

    

