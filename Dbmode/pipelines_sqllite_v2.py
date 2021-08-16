# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter

# Pipelines using sqlite3

class PaperscrapPipeline:

    def __init__(self):
        self.CreateConn()
        self.CreateTable()

    def CreateConn(self):
        self.conn=sqlite3.connect("CitationData.db")
        self.curr=self.conn.cursor()

    def CreateTable(self):
        self.curr.execute(""" DROP TABLE IF EXISTS Cite_Data""")
        self.curr.execute(""" create table Cite_Data(
                Author text,
                Title text,
                Date text,
                Citation text,
                Reference text
                )
                 """)

    def process_item(self, item, spider):
        
        self.Store_db(item)
        print("-------------------------------------------------------------------------------------")
        print("Pipeline: ",item['author'])
        print("-------------------------------------------------------------------------------------")
        return item

    def Store_db(self,item):
        cit_string=""
        ref_string=""
        aut_string=""

        for i in item['author']:
            aut_string+=i+","

        for i in item['citations']:
            cit_string+=i+","

        for i in item['reference']:
            ref_string+=i+","

        cit_string=cit_string[:-1]
        ref_string=ref_string[:-1]
        aut_string=aut_string[:-1]

        self.curr.execute( """INSERT INTO Cite_Data VALUES(?,?,?,?,?) """ , ( aut_string,item['title'][0],item['date'][0],cit_string,ref_string )  )
        self.conn.commit()