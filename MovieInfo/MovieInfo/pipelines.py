# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import datetime

class MovieinfoPipeline:

    """
    文件格式
    title director actor
    x,xx,xxx
    """
    keys = ["title", "director", "actor", "duration", "movie_image",
            "rating", "release_date", "type", "language", "spider"]

    def __init__(self):
        pass

    def open_spider(self, spider):
        csv_filename = "{}_{}.csv".format(spider.name, datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        self.file = open(csv_filename, "a", encoding="utf-8", newline="")
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow(self.keys)

    def process_item(self, item, spider):
        print("管道输入：", item)
        item_values = []
        for key in self.keys[:-1]:
            value = item.get(key, " ")
            item_values.append(value)
        item_values.append(spider.name)
        self.csv_writer.writerow(item_values)
        return item

    def close_spider(self, spider):
        self.file.close()

