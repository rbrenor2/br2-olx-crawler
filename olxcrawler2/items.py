# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Olxcrawler2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class IphoneOfferItem(scrapy.Item):
    product_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    post_date = scrapy.Field()
    post_time = scrapy.Field()
    thumb_url = scrapy.Field()
    is_featured = scrapy.Field()
    list_position = scrapy.Field()
    scrap_time = scrapy.Field()