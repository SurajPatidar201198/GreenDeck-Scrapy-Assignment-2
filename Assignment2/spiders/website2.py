import scrapy
import re

class PaginationSpider(scrapy.Spider):
    name = 'website2'
    allowed_domains = ['www.farfetch.com']      
    start_urls = ['https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page=1']

   
    total_pages=93    #total_pages need to be scrapped
    nextpage=1
    def parse(self, response):
        #zipping all the name,brand,price,product_URL,Image_URL list and taking entries from them
        for i,j,k,m,l in zip(response.xpath("//p[@itemprop='name']//text()").getall(),response.xpath("//h3[@itemprop='brand']//text()").getall(),response.xpath("//span[@data-test='price']/text()").getall(),response.xpath('//*[@class="_5ce6f6"]//@href').getall(),response.xpath('//meta[@itemprop="image"]//@content').getall()):
            yield{
                "Name":i,
                "Brand":j,
                "Price":k,
                "Product_URL":"https://www.farfetch.com/"+m,
                "Image_URL":l
            }

        #iterating over next pages
        if self.nextpage <= self.total_pages:
            self.nextpage+=1
            next_page = "https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?page=" + str(self.nextpage)
            # print("Current_page:" + str(self.nextpage))
            yield response.follow(url=next_page, callback=self.parse)

