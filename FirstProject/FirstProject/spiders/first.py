import scrapy
from lxml import etree

class FirstSpider(scrapy.Spider):
    name = "first"
    allowed_domains = ["spbeen.com"]
    start_urls = ["http://spbeen.com"]

    def parse(self, response):
        # 定义解析数据
        item = {}
        # 获取标题
        item['title'] = response.xpath('.//title/text()').extract()
        print('First Spider item：', item)
        # 返回数据 进入管道
        return item