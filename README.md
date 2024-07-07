**安装scrapy框架**

```shell
# 版本 2.11.2
pip install scrapy
```

**测试命令**

```shell
scrapy shell www.baidu.com
```

**创建项目**

```shell
scrapy startproject [name]
```

**创建爬虫**

```shell
# 按照模版格式创建爬虫文件 template=basic(基础的爬虫模版) | crawl(网址匹配的爬虫模版文件)
scrapy genspider -t [template] [name] [domain]

scrapy genspider -t basic basic01 baidu.com
scrapy genspider -t crawl crawl02 baidu.com
scrapy genspider -t csvfeed csvfeed03 baidu.com
scrapy genspider -t xmlfeed xmlfeed04 baidu.com
```

**启动爬虫**

```shell
# name=爬虫名称
scrapy crawl [name]
```

**命令调试**

```shell
scrapy shell [domain]
```

**查看版本**

```shell
scrapy version
```

**性能检查**

```shell
scrapy bench
```

**如果想使用ImagesPipeline的pipeline**

```shell
pip install Pillow
```

**liunx安装scrapyd**

```shell
pip install scrapyd
```

**开发端安装scrapyd-client**

```shell
pip install scrapyd-client
```

**部署命令**

```shell
scrapyd-deploy -a -p [project_name]
```

**安装redis**

```shell
pip install redis
```

**安装pymysql**

```shell
pip install pymysql
```

**安装web管理端**

```shell
pip install spider-admin-pro
```

**启动web管理端**

```shell
gunicorn --bind '0.0.0.0:8000' 'spider_admin_pro.main:app'
```

