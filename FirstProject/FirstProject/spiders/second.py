import scrapy


class SecondSpider(scrapy.Spider):
    name = "second"
    allowed_domains = ["spbeen.com"]
    start_urls = ["http://www.spbeen.com/tool/request_info/"]

    def parse(self, response):
        ua_message = response.xpath('.//div[@class="content"]/div/div[2]/div[2]/text()').extract()
        print("爬取结果:", ua_message)
