import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from homegate_scrapy.items import HomegateScrapyItem


class TgbusSpider(CrawlSpider):

    name = 'tgbus'
    allowed_domains = ['tgbus.com']
    start_urls = [
        'http://www.tgbus.com'
    ]

    rules = [
        Rule(
            SgmlLinkExtractor(
                restrict_xpaths='//div[@id="tpc1_01"]//ul//li'
            ),
            callback='parse_item',

        ),
    ]

    def parse_item(self, response):
        title = response.xpath(
            '//div[@class="content bdr"]//h1/text()').extract()

        if title:
            parsed_link = self.parse_from_link(response.url)
            if parsed_link:
                title = title[0]
                link = response.url
                content = response.xpath(
                    '//div[@class="text"]//text()').extract()
                content = content[0]

                item = HomegateScrapyItem()
                item['title'] = title
                item['link'] = link
                item['identity'] = parsed_link[1]
                item['site'] = self.name
                return item

    def parse_from_link(self, link):
        m = re.search("http://(\w+).tgbus.com/([0-9a-z]+)/([0-9a-z]+)/([0-9a-z]+)/(\d+).shtml$", link)

        if m:
            groups = m.groups()
            return groups[0], groups[-1]
        else:
            m = re.search("http://(\w+).tgbus.com/([0-9a-z]+)/([0-9a-z]+)/(\d+).shtml$", link)
            if m:
                groups = m.groups()
                return groups[0], groups[-1]
