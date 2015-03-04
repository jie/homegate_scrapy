
import scrapy
from scrapy.selector import Selector
from datetime import datetime
from homegate_scrapy.items import HomegateScrapyItem


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = [
        'https://github.com/trending?since=daily',
    ]

    sitePrefix = 'https://www.github.com'
    showcase = 'coding'

    def parse(self, response):
        for item_html in response.xpath('//li[@class="repo-list-item"]').extract():
            item = Selector(text=item_html)
            link = item.xpath('//h3/a/@href').extract()[0]
            title = self.parse_title(link)
            description = item.xpath('//p[@class="repo-list-description"]/text()').extract()
            description = description[0].strip() if description else ''
            github_item = HomegateScrapyItem()
            github_item['site'] = self.name
            github_item['link'] = "%s%s" % (self.sitePrefix, link)
            github_item['description'] = description
            github_item['title'] = title
            github_item['identity'] = link
            github_item['create_at'] = datetime.now()
            github_item['showcase'] = self.showcase
            yield github_item

    def parse_title(self, title):
        return title.split('/')[-1]
