# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HomegateScrapyItem(scrapy.Item):

    title = scrapy.Field()
    link = scrapy.Field()
    identity = scrapy.Field()
    site = scrapy.Field()
    content = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    tag = scrapy.Field()
    showcase = scrapy.Field()
    create_at = scrapy.Field()
