import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from tuchuzy.items import Product


class ProductCrawlSpider(CrawlSpider):
    item_category = ''
    name = 'tuchuzy'
    allowed_domains = ['tuchuzy.com']
    start_urls = ['https://www.tuchuzy.com/']
    denied_urls = ['https://www.tuchuzy.com/collections/new-arrivals',
                   'https://www.tuchuzy.com/collections/back-in-stock',
                   'https://www.tuchuzy.com/collections/exclusives',
                   'https://www.tuchuzy.com/collections/best-sellers'
                   ]

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//span[contains(text(), 'By Category')]"
                            "/following-sibling::ul/li"
                            "/a[contains(@href,'/collections/') and not(contains(text(), 'View All'))]",
            deny=denied_urls,
        ), callback='parse_category'),
    )

    def parse_category(self, response):

        next_page = response.css('link[rel="next"]::attr(href)').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_category)

        for item in response.css('div[class^="product-grid-item grid__item xlarge-up--one-quarter one-half"]'):
            l = ItemLoader(item=Product(), response=response)
            l.add_value('category', self.get_category(response))
            if text_fields := item.css('a > div[class="product-text"]'):
                l.selector = text_fields
                l.add_css('name', 'p.title *::text')
                l.add_css('brand', 'h2 *::text')
                if product_on_sale := item.css('p[class*="sale"]'):
                    l.selector = product_on_sale
                    l.add_css('price', 's *::text')
                    l.add_css('sale_price', 'span[itemprop="price"] *::text')
                else:
                    l.add_css('price', 'p.price > span *::text')
            if image_fields := item.css('a > div[class="product-image"]'):
                l.selector = image_fields
                l.add_css('image_links', 'img::attr(srcset)')
            yield l.load_item()

    def get_category(self, response):
        for t in response.css('li[class^="site-nav--has-submenu main-menu"]'):
            self.item_category = t.css('a *::text').extract_first().strip()

        for category in response.css('ul.site-nav__subsubmenu > li > a'):
            if category.css('::attr(href)').extract_first() in response.url:
                return self.item_category + ">>" + category.css('::text').extract_first().strip()
