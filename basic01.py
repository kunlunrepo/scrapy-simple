import scrapy


class Basic01Spider(scrapy.Spider):
    # 爬虫名
    name = "basic01"
    # 允许的域名
    allowed_domains = ["baidu.com"]
    # 起始URL
    start_urls = ["https://baidu.com"]

    # 处理逻辑
    def parse(self, response):
        pass
