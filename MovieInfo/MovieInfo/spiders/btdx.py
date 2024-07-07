import scrapy


class BtdxSpider(scrapy.Spider):
    name = "btdx"
    allowed_domains = ["btdx8.vip"]
    start_urls = ["https://www.btdx8.vip/category/kehuan"]
    host = 'https://www.btdx8.vip'

    def parse(self, response):
        # print("爬虫输入：", response.body)

        movies_element = response.xpath(".//div[@id='content']/div[2]/div[@id]")
        for movie in movies_element:
            # 列表：extract() get_all() 第一个：extract_first() get()
            link = movie.xpath("./a/@href").extract_first()
            # print(self.host, link)
            url = "{}{}".format(self.host, link)
            # print(url)
            # return scrapy.Request(url=url, callback=self.parse_movie_detail)
            yield scrapy.Request(url=url, callback=self.parse_movie_detail)


    def parse_movie_detail(self, response):
        info_list = response.xpath('.//div[@id="movie_info"]//text()').extract()
        info_list = [info.replace('\u3000', '').replace('\n', '') for info in info_list]
        print(info_list)
        actor_number = [info_list.index(info) for info in info_list if "主演" in info]
        alias_number = [info_list.index(info) for info in info_list if "译名" in info]
        # print(actor_number, alias_number)
        # for info in info_list:
        #     print(info)
        item = {}
        item['title'] = "".join([info.replace('片名', '') for info in info_list if "片名" in info])
        item['director'] = "".join(info_list[:actor_number[0]]).replace("导演:", "")
        item['actor'] = "".join(info_list[actor_number[0]: alias_number[0]]).replace("导演:", "")
        item['duration'] = "".join([info.replace('片长', '') for info in info_list if "片长" in info])
        item['movie_image'] = response.xpath('.//div[@id="poster_src"]/img/@src').get()
        item['rating'] = "".join([info.replace('豆瓣评分', '') for info in info_list if "豆瓣评分" in info])
        item['release_date'] = "".join([info.replace('上映日期', '') for info in info_list if "上映日期" in info])
        item['type'] = "".join([info.replace('类别', '') for info in info_list if "类别" in info])
        item['language'] = "".join([info.replace('语言', '') for info in info_list if "语言" in info])
        item['info_source'] = response.xpath('.//div[@class="poster"]').get()
        print(item)
