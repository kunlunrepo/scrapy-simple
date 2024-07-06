from scrapy.spiders import XMLFeedSpider


class Xmlfeed04Spider(XMLFeedSpider):
    name = "xmlfeed04"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]
    iterator = "iternodes"  # you can change this; see the docs
    itertag = "item"  # change it accordingly

    def parse_node(self, response, selector):
        item = {}
        #item["url"] = selector.select("url").get()
        #item["name"] = selector.select("name").get()
        #item["description"] = selector.select("description").get()
        return item
