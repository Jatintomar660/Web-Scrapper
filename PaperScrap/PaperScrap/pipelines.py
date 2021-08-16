# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class PaperscrapPipeline:

    def __init__(self):
        self.Conn=pymongo.MongoClient(
            'localhost',
            27017
        )
        db=self.Conn['MyQuotes'] #create database
        self.collection=db['Quotes_tb'] #create table in db

    def process_item(self, item, spider):
        
        self.collection.insert(dict(item))
        print("-------------------------------------------------------------------------------------")
        print("Pipeline: ",item['author'])
        print("-------------------------------------------------------------------------------------")
        return item

