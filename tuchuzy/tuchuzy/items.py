# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    category = scrapy.Field()
    image_links = scrapy.Field()
    price = scrapy.Field(serializer=str)
    sale_price = scrapy.Field(serializer=str)
