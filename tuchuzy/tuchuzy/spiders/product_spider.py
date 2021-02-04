from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ProductCrawlSpider(CrawlSpider):
    name = 'tuchuzy'
    allowed_domains = ['tuchuzy.com']
    start_urls = ['https://www.tuchuzy.com/']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(restrict_css=("li[class^='site-nav--has-submenu main-menu']",)), callback='parse_item'),
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        # Rule(LinkExtractor(allow=('item\.php',)), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)

        _count = 0
        for test in response.css("div[class^='product-grid-item grid__item xlarge-up--one-quarter one-half']"):
            _count += 1
            self.logger.info(_count)

        # l = ItemLoader(item=Product(), response=response)
        #
        # name = scrapy.Field()
        # l.add_css('name', '.title')
        # brand = scrapy.Field()
        # l.add_css('brand', '.vendor h5')
        # category = scrapy.Field()
        # image_links = scrapy.Field()
        # price = scrapy.Field(serializer=str)
        # sale_price = scrapy.Field(serializer=str)
        #
        # l.add_css('name', '.title')
        # l.add_xpath('price', '//p[@id="price"]')
        # l.add_css('stock', 'p#stock]')
        # l.add_value('last_updated', 'today')  # you can also use literal values
        # return l.load_item()

        # item = scrapy.Item()
        # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        # item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
        # item['link_text'] = response.meta['link_text']
        # url = response.xpath('//td[@id="additional_data"]/@href').get()
        # return response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))

    # def parse_additional_page(self, response, item):
    #     item['additional_data'] = response.xpath('//p[@id="additional_data"]/text()').get()
    #     return item
