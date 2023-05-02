# from datetime import datetime
# import os
# import scrapy
# class MySpider(scrapy.Spider):
#     name = 'navo'
#     start_urls = []
#     for i in range(1,10):
#         a = str(i)
#         b = 'https://navodesk.com/shop/page/'+ a +'/'
#         if(b in start_urls):
#             break
#         else:
#             start_urls.append(b)
#
#     def __init__(self):
#         super(MySpider, self).__init__()
#         self.directory_path = input("enter the directory: ")
#
#     def parse(self, response):
#         # Extract the product URLs from the page
#         urls = response.css('a.woocommerce-LoopProduct-link::attr(href)').getall()
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse_product)
#
#     def parse_product(self, response):
#         product_sku = response.css(".sep+ .mg-brand-wrapper::text").get()
#         if product_sku:
#             filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + " " + product_sku + '.html'
#         else:
#             filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.html'
#         full_path = os.path.join(self.directory_path, filename)
#         # Save file
#         with open(full_path, 'wb') as f:
#             f.write(response.body)
