import scrapy


class Douban250Spider(scrapy.Spider):
    name = "douban250"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'CONCURRENT_REQUESTS': 2,
        'ITEM_PIPELINES': {
            "MovieInfo.pipelines.MovieinfoPipeline": 300,
        }
    }

    def parse(self, response):
        movie_elements = response.xpath('.//ol[@class="grid_view"]/li')
        for movie in movie_elements:
            link = movie.xpath('./div/div[2]/div/a/@href').get()
            title = movie.xpath('./div/div[2]/div/a/span[1]/text()').get()
            print(title, link)
            yield scrapy.Request(link, callback=self.parse_movie_detail)

    def parse_movie_detail(self, response):
        item={}
        item['title'] = response.xpath('.//span[@property="v:itemreviewed"]/text()').get()
        item['director'] = "".join(response.xpath('.//div[@id="info"]/span[1]/span[2]/a/text()').extract())
        item['actor'] = "".join(response.xpath('.//div[@id="info"]/span[1]/span[2]/a/text()').extract())
        item['duration'] = response.xpath('.//span[@property="v:runtime"]/text()').get()
        item['movie_image'] = response.xpath('.//div[@id="mainpic"]/a/img/@src').get()
        item['rating'] = response.xpath('.//strong[@property="v:average"]/text()').get()
        item['release_date'] = "".join(response.xpath('.//span[@property="v:initialReleaseDate"]/text()').extract())
        item['type'] = "".join(response.xpath('.//span[@property="v:genre"]/text()').extract())
        item['language'] = ""
        item['info_source'] = response.xpath('.//div[@id="info"]').get()

        # print(item)
        yield item
