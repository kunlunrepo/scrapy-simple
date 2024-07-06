from scrapy.spiders import CSVFeedSpider


class Csvfeed03Spider(CSVFeedSpider):
    name = "csvfeed03"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://baidu.com"]
    #headers = ["id", "name", "description", "image_link"]
    #delimiter = "\t"

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        #i["url"] = row["url"]
        #i["name"] = row["name"]
        #i["description"] = row["description"]
        return i
