import scrapy
from ..items import PaperscrapItem

class QuoteSpider(scrapy.Spider):
        name='quotes' # name of spider
        # list of spider
        
        url_list=[]
        start_urls=["https://www.researchgate.net/publication/2524595_PageRank_Computation_and_the_Structure_of_the_Web_Experiments_and_Algorithms"]

        def parse(self,response):
            items=PaperscrapItem()
            aut=response.css(".nova-v-person-list-item__align")
            Ref_obj=response.css(".js-target-reference")
            Cit_Obj=response.css(".js-target-citation")

            items['title']=response.css(".research-detail-header-section__title::text").extract()
            items['author']=aut.css(".nova-e-link--theme-bare::text").extract()
            items['date']=response.css(".nova-e-text--color-grey-700 .nova-e-list__item::text").extract()
            items['citations']=Cit_Obj.css(".nova-e-link--theme-bare::text").extract()
            items['reference']=Ref_obj.css(".nova-e-link--theme-bare::text").extract()
            
            yield items

            QuoteSpider.url_list=Cit_Obj.css(".nova-e-link--theme-bare::attr(href)").extract()
            QuoteSpider.url_list+=Ref_obj.css(".nova-e-link--theme-bare::text").extract()

            print("********************************************************")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(QuoteSpider.url_list)
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("********************************************************")
            for i in QuoteSpider.url_list:
                # print(i)
                yield response.follow(i,meta = {'dont_redirect': True,'handle_httpstatus_list': [301,302]},callback=self.parse)

            # all_quotes=response.css("div.quote")
            # for i in all_quotes:
            #     Text=i.css(".text::text").extract()
            #     author=i.css(".author::text").extract()
            #     Tags=i.css(".tag::text").extract()

            #     items['text']=Text
            #     items['author']=author
            #     items['tags']=Tags

            #     yield items
            
            # NextPage=response.css("li.next a::attr(href)").get()
            # if(NextPage is not None):
            #     yield response.follow(NextPage,callback=self.parse)