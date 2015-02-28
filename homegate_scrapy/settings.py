# -*- coding: utf-8 -*-

# Scrapy settings for homegate_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'homegate_scrapy'

SPIDER_MODULES = ['homegate_scrapy.spiders']
NEWSPIDER_MODULE = 'homegate_scrapy.spiders'

ITEM_PIPELINES = {
    'homegate_scrapy.pipelines.HomegateScrapyPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'homegate_scrapy (+http://www.yourdomain.com)'

LOG_LEVEL = 'ERROR'
# LOG_ENABLED = False

DATABASE = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'homegate',
    'passwd': 'homegate',
    'db': 'homegate',
    'charset': 'utf8'
}

