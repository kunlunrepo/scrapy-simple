import scrapy
import datetime


class NcovSpider(scrapy.Spider):
    name = "ncov"
    allowed_domains = ["ncovdata.spbeen.com"]
    # start_urls = [
    #     "http://ncovdata.spbeen.com/apis/get_china_provinces/?query_date=2020-01-31",
    # ]
    base_url = "http://ncovdata.spbeen.com/apis/get_china_provinces/?query_date={}"

    # 发起请求 代替start_urls
    def start_requests(self):
        start_date_str = '2020-01-26'
        # 起始日期
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        for i in range(0, 15):
            #当前日期
            current_date = start_date + datetime.timedelta(days=i)
            current_url = self.base_url.format(current_date.strftime("%Y-%m-%d")) # 日期转字符串
            # 发起请求 只有生成器才能被框架一直调用
            yield scrapy.Request(url=current_url, callback=self.parse)

    def parse(self, response):
        # 查找的省份
        province = "江西"
        item = {province: {}}
        # 请求获取到的数据
        data_list = response.json()["data"]
        for province_data in data_list:
            if province in str(province_data):
                item = province_data
                item['source'] = response.text
                break
        else: # break打断循环 打断后else会执行
            item={}
            item['source'] = ''
        # print(item)
        # 返回数据
        return item