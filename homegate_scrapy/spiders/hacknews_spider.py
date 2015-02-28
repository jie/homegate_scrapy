from scrapy import log
from scrapy.contrib.spiders import XMLFeedSpider
from homegate_scrapy.items import HomegateScrapyItem


class HacknewsSpider(XMLFeedSpider):
    name = 'hacknews'
    allowed_domains = ['news.ycombinator.com']
    start_urls = [
        'https://news.ycombinator.com/rss'
    ]
    # This is actually unnecessary, since it's the default value
    iterator = 'iternodes'
    itertag = 'item'

    IdentitySep = 'https://news.ycombinator.com/item?id='

    def parse_node(self, response, node):
        item = HomegateScrapyItem()
        item['title'] = node.xpath('title/text()').extract()[0]
        item['link'] = node.xpath('link/text()').extract()[0]
        comment = node.xpath('comments/text()').extract()[0]
        item['identity'] = self._parse_id(comment)
        return item

    def _parse_id(self, comment):
        _, identity = comment.split(self.IdentitySep)
        return identity
