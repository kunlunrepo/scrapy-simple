from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    settings = get_project_settings()

    # 创建爬虫线程，启动多个爬虫
    crawler = CrawlerProcess(settings)
    crawler.crawl('douban250') # 爬虫名
    crawler.crawl('btdx') # 爬虫名
    crawler.start()