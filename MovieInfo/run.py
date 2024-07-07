"""该文件仅用于调试"""

import os
from scrapy.cmdline import execute

if __name__ == '__main__':
    # execute("scrapy", "crawl", "first")
    execute("scrapy crawl douban250".split())
    # execute("scrapy crawl btdx".split())