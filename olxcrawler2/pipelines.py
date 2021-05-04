# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime, timedelta

class Olxcrawler2Pipeline:
    def process_item(self, item, spider):
        return item

class IphoneOfferPipeline:
    def process_item(self, offerItem, spider):
        if offerItem['post_time'] is not None and 'às' in offerItem['post_time']:
            offerItem["post_date"] = self.getDate(offerItem["post_time"].split(' às ')[0])
            offerItem["post_time"] = offerItem["post_time"].split(' às ')[1]
        
        if offerItem["price"] is not None:
            offerItem["price"] = float(offerItem["price"].split("R$ ")[1].replace('.', ''))
            
        offerItem["is_featured"] = True if offerItem['is_featured'] == '1' else False
        offerItem["list_position"] = int(offerItem['list_position'])

        if offerItem["city"] is not None and offerItem["city"] != '':
                offerItem["state"] = offerItem["city"].split(' - ')[1].replace(' ', '')
                offerItem["city"] = offerItem["city"].split(' - ')[0]
        else:
            offerItem["city"] = None
            offerItem["state"] = None

        return offerItem

    def getDate(self, date):
        if date == 'Hoje':
            return datetime.now().strftime('%Y-%m-%d')
        elif date == 'Ontem':
            return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        else:
            # date_formatted = self.formatDate(date)
            return datetime.now().strftime('%Y-') + datetime.strptime(date, '%d/%m').strftime('%m-%d')        

    def formatDate(self, date):
        if date == 'fev':
            return date.replace('fev', 'feb')
        elif date == 'abr':
            return date.replace('abr', 'apr')
        elif date == 'mai':
            return date.replace('mai', 'may')
        elif date == 'ago':
            return date.replace('ago', 'aug')
        elif date == 'set':
            return date.replace('set', 'sep')
        elif date == 'out':
            return date.replace('out', 'oct')
        elif date == 'dez':
            return date.replace('dez', 'dec')
