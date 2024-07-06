import scrapy
from scrapy.pipelines.images import ImagesPipeline


class DownloadimageSpider(scrapy.Spider):
    name = "downloadImage"
    allowed_domains = ["angelimg.spbeen.com"]
    start_urls = ["http://angelimg.spbeen.com"]

    def parse(self, response):
        image_urls = response.xpath(".//img/@src").extract()
        for image_url in image_urls:
            if 'http://' in image_url or 'https://' in image_url:
                pass
            else:
                image_urls.remove(image_url)

        item = dict()

        item['files'] = []
        item['file_urls'] = image_urls

        item['images'] = []
        item['image_urls'] = image_urls

        print(image_urls)
        return item