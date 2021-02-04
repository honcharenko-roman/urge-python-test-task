# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import CloseSpider


class TuchuzyPipeline:
    LIMIT = 100
    current_number = 0

    def process_item(self, item, spider):
        if self.current_number >= self.LIMIT:
            raise CloseSpider('limit reached')
        self.current_number += 1
        return item
