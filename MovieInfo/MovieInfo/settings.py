# Scrapy settings for MovieInfo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "MovieInfo"

SPIDER_MODULES = ["MovieInfo.spiders"]
NEWSPIDER_MODULE = "MovieInfo.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "MovieInfo (+http://www.yourdomain.com)"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.1

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   # "Accept-Language": "en",
    "Cookie": "guardok=3E2oT/24uxnvU+iXDZTiyoAPhA8DbOVGgQ7QjzRww1B8oG45NqQqEko86mF72W3VvIJfYZa1ZLBR00xh8KxcDg==; __51uvsct__KSHZstkfsUdSd0XT=1; __51vcke__KSHZstkfsUdSd0XT=e166a672-1a83-54fe-9eb0-1a582f176e9c; __51vuft__KSHZstkfsUdSd0XT=1720321916719; Hm_lvt_99227487c7b463737ebb51a4713742c9=1720321917; HMACCOUNT=51DC1C1ABE99C8AD; _ga=GA1.2.1934624663.1720321917; _gid=GA1.2.1031714068.1720321917; _ym_uid=1720321919522466325; _ym_d=1720321919; Hm_lpvt_99227487c7b463737ebb51a4713742c9=1720321920; __vtins__KSHZstkfsUdSd0XT=%7B%22sid%22%3A%20%22742be1b9-2aa3-51ac-8589-a057ed6f9fce%22%2C%20%22vd%22%3A%202%2C%20%22stt%22%3A%203052%2C%20%22dr%22%3A%203052%2C%20%22expires%22%3A%201720323719769%2C%20%22ct%22%3A%201720321919769%7D; _ym_isad=2; _ym_visorc=w"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "MovieInfo.middlewares.MovieinfoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "MovieInfo.middlewares.MovieinfoDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "MovieInfo.pipelines.MovieinfoPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
