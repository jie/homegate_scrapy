# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pony.orm
from database import Hacknews


class HomegateScrapyPipeline(object):

    def process_item(self, item, spider):
        with pony.orm.db_session:
            if spider.name == 'hacknews':
                try:
                    news = Hacknews.get(identity=item['identity'])
                except pony.orm.ObjectNotFound:
                    news = None

                if not news:
                    Hacknews(**item)
                    pony.orm.flush()
                    pony.orm.commit()

        return item
