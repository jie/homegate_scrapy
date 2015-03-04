# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pony.orm
from database import News


class HomegateScrapyPipeline(object):

    def process_item(self, item, spider):

        if item:
            with pony.orm.db_session:
                try:
                    news = News.get(
                        identity=item['identity'],
                        site=item['site']
                    )
                except pony.orm.ObjectNotFound:
                    news = None

                if not news:
                    News(**item)
                    pony.orm.flush()
                    pony.orm.commit()
                else:
                    if item.get('create_at'):
                        news.create_at = item['create_at']
                        pony.orm.flush()
                        pony.orm.commit()

        return item
