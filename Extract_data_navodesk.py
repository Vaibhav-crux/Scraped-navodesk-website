import re
import scrapy
import datetime
import json
class MySpider(scrapy.Spider):
    name = 'navo'
    start_urls = []

    for i in range(1, 10):
        a = str(i)
        b = 'https://navodesk.com/shop/page/' + a + '/'
        if (b in start_urls):
            break
        else:
            start_urls.append(b)

    def parse(self, response):
        # Extract the product URLs from the page
        urls = response.css('a.woocommerce-LoopProduct-link::attr(href)').getall()

        # Print the product URLs
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_product, meta={'url': url})

    def parse_product(self, response):
        url = response.meta.get('url')
        yield {
            'Having': url
        }
    EXTRACT PRODUCT COLOUR
        product_colour = response.css(
            'ul.variable-items-wrapper.color-variable-items-wrapper li.variable-item[data-value]:not([data-value=""])::attr(data-value)').getall()
        product_colour += response.css('div.variable-item-contents img.variable-item-image::attr(alt)').getall()
        product_colour += response.css('select[name="attribute_color"] option[value]:not([value=""])::text').getall()
        product_colour += response.css('select#colors option:not(:first-child)::attr(value)').getall()
        product_colour_arr = []
        for colour in product_colour:
            product_colour_arr.append(colour)
    # EXTRACT PRODUCT TITLE
        title = response.css('.entry-title::text').get()
    # EXTRACT PRODUCT SKU
        product_sku = response.css(".sep+ .mg-brand-wrapper::text").get()
    # EXTRACT PRODUCT BRAND NAME
        brand = response.css('.pwb-clearfix a::text').get()
        brands = brand.replace('Brand :','')
        brand = ""
        for brands in brands:
            if(brands.isalpha()):
                brand += brands
    # EXTRACT PRODUCT STOCK
        quantity = response.xpath('//input[@max]/@max').get()
    # EXTRACT PRODUCT LINK
        url = response.meta.get('url')
    # EXTRACT PRODUCT NUMBERS OF REVIEWS
        review = response.css('.count::text').get()
    # EXTRACT PRODUCT DETAILS
        product_detail = response.css('#productTitle::text').get()
    # CURRENT DATE AND TIME
        today = datetime.datetime.now()
        today = today.strftime("%b-%d-%Y %H:%M:%S")
    # EXTRACT PRODUCT RETURN POLICY
        return_policy = response.css('#tab-shipping_returns p::text').get()
    # EXTRACT PRODUCT WEIGHT
        weight = response.css('.pro-extra-item::text').get()
        weight_sum = ""
        for weights in weight:
            if (weights.isalpha() or weights.isdigit() or weights == "."):
                weight_sum += weights
    # EXTRACT PRODUCT PRICE
        cost = response.css('bdi::text').get()
        product_cost_str = ""
        for costs in cost:
            cost_str = str(costs)
            if (cost_str.isdigit() or cost_str == "."):
                product_cost_str += cost_str

        plus = 0 #It will incerement by 1 each time loop begins and print product colour one by one
    #If data-product_variations= is present in VIEW SOURCE PAGE
        try:
            data = re.findall('data-product_variations="(.*?)"><table class="variations"', response.text, re.DOTALL)[
                0].replace("&quot;", '"')
        #LOADS THE JSON DATA
            json_datas = json.loads(data)
        #LOOP FOR EACH PRODUCT JSON DATA
            for curr_data in json_datas:
            #WHEN THE COLOUR OF PRODUCT IS PRESENT
                if(len(product_colour_arr)>0):
                    yield {
                        'maximum': curr_data["max_qty"],
                        'sku': product_sku,
                        'Cost': curr_data['display_price'],
                        'Color': product_colour_arr[plus],
                        'length': curr_data['dimensions']['length'],
                        'width': curr_data['dimensions']['width'],
                        'height': curr_data['dimensions']['height'],
                        'weight': weight_sum,
                        'title': curr_data['image']['title'],
                        'url': url,
                        'review': review,
                        'Product detail': product_detail,
                        'Return Policy': return_policy,
                        'Date and Time': today,
                        'Brand': brand
                    }
                    plus +=1

                else:
                    # WHEN THE COLOUR OF PRODUCT IS NOT PRESENT
                    yield {
                        'maximum': curr_data["max_qty"],
                        'sku': product_sku,
                        'Cost': curr_data['display_price'],
                        'Color': None,
                        'length': curr_data['dimensions']['length'],
                        'width': curr_data['dimensions']['width'],
                        'height': curr_data['dimensions']['height'],
                        'weight': weight_sum,
                        'title': curr_data['image']['title'],
                        'url': url,
                        'review': review,
                        'Product detail': product_detail,
                        'Return Policy': return_policy,
                        'Date and Time': today,
                        'Brand': brand
                    }
    # If data-product_variations= is present not in VIEW SOURCE PAGE then extract data from web page
        except:
        # WHEN THE COLOUR OF PRODUCT IS PRESENT
            if(len(product_colour_arr)>0):
                yield {
                    'maximum': quantity,
                    'sku': product_sku,
                    'Cost': product_cost_str,
                    'Color': product_colour_arr[plus],
                    'length': None,
                    'width': None,
                    'height': None,
                    'weight': weight_sum,
                    'title': title,
                    'url': url,
                    'review': review,
                    'Product detail': product_detail,
                    'Return Policy': return_policy,
                    'Date and Time': today,
                    'Brand': brand
                }
                plus +=1
            else:
            # WHEN THE COLOUR OF PRODUCT IS NOT PRESENT
                yield {
                    'maximum': quantity,
                    'sku': product_sku,
                    'Cost': product_cost_str,
                    'Color': None,
                    'length': None,
                    'width': None,
                    'height': None,
                    'weight': weight_sum,
                    'title': title,
                    'url': url,
                    'review': review,
                    'Product detail': product_detail,
                    'Return Policy': return_policy,
                    'Date and Time': today,
                    'Brand': brand
                }