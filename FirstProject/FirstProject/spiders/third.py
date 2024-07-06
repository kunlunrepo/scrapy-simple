import scrapy


class ThirdSpider(scrapy.Spider):
    name = "third"
    allowed_domains = ["shanzhi.spbeen.com"]
    start_urls = ["http://shanzhi.spbeen.com/detail/?id=3917"]

    def parse(self, response):
        print(response.text)
        print(response.url)
