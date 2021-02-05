# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose
from scrapy.loader.processors import TakeFirst


def transform_price(value: str):
    return value.replace('$', '').replace('.', '')


def transform_srcset(value: str):
    return value.replace('//', '')


def get_highest_resolution(value: str):
    return value.split(', ')[-1].split(' ')[0].strip()


class Product(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    brand = scrapy.Field(input_processor=MapCompose(str.upper),
                         output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
    image_links = scrapy.Field(
        input_processor=MapCompose(str.strip, transform_srcset, get_highest_resolution),
    )
    price = scrapy.Field(
        input_processor=MapCompose(transform_price),
        output_processor=TakeFirst()
    )
    sale_price = scrapy.Field(
        input_processor=MapCompose(transform_price),
        output_processor=TakeFirst()
    )
