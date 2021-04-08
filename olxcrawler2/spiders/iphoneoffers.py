# -*- coding: utf-8 -*-
import scrapy
from ..items import IphoneOfferItem


class IphoneoffersSpider(scrapy.Spider):
    name = 'iphoneoffers'
    allowed_domains = ['http://www.olx.com.br/', 'www.olx.com.br']
    start_urls = ['http://www.olx.com.br/celulares/iphone/usado?q=iphone/']

    def parse(self, response):
        offerItem = IphoneOfferItem()
        offerList = response.css('.gIEtsI')
        for offer in offerList:
            offerItem["title"] = offer.xpath("//h2[contains(@class, 'jyXVpA')]/text()").get()
            offerItem["price"] = offer.xpath("//span[contains(@class,'eoKYee')]/text()").get()
            locality = offer.xpath(".//span[contains(@class,'dpURtf')]/text()").get()
            if locality is not None and locality != '':
                offerItem["city"] = locality.split(' - ')[0]
                offerItem["state"] = locality.split(' - ')[1]
            else:
                offerItem["city"] = None
                offerItem["state"] = None

            yield offerItem

        nextPageUrl = offer.xpath(""".//a[contains(@class,'sc-1bofr6e-0') and contains(@class, 'iRQkdN') and @data-lurker-detail='next_page']/@href""").get()
        print('nextpage')
        print(nextPageUrl)
        if nextPageUrl is not '' and nextPageUrl is not None:
            print('Proxima pagina')
            yield response.follow(url=nextPageUrl, callback=self.parse)



