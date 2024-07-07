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


import redis
import json

class MovieinfoRedisPipeline:
    def open_spider(self, spider):
        self.conn = redis.Redis(host="192.168.10.55", port=6379, db=0, password='base@GO5r1Ydsb6H')

    def process_item(self, item, spider):
        if item.get("title", False):
            self.conn.set(item["title"], json.dumps(item))
        return item

    def close_spider(self, spider):
        self.conn.close()

import pymysql
class MovieinfoMysqlPipeline:

    database='moveinfo'
    table='movie_infos'

    def open_spider(self, spider):
        self.conn = pymysql.connect(host="192.168.10.55", port=3306, db=self.database,
                                    user="root", password="base@GO5r1Ydsb6H", charset="utf8")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS `{self.table}` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `title` varchar(255) DEFAULT NULL,
          `director` varchar(255) DEFAULT NULL,
          `actor` varchar(255) DEFAULT NULL,
          `duration` varchar(255) DEFAULT NULL,
          `movie_image` varchar(255) DEFAULT NULL,
          `rating` varchar(255) DEFAULT NULL,
          `release_date` varchar(255) DEFAULT NULL,
          `type` varchar(255) DEFAULT NULL,
          `language` varchar(255) DEFAULT NULL,
          `info_source` text,
          `spider` varchar(255) DEFAULT NULL,
          PRIMARY KEY (`id`)
          );
          """
        self.cursor.execute(create_table_sql)
        self.conn.commit()


    def process_item(self, item, spider):
        if item.get("title", False):
            insert_sql = f"""
            INSERT INTO `{self.table}` (
              `title`,
              `director`,
              `actor`,
              `duration`,
              `movie_image`,
              `rating`,
              `release_date`,
              `type`,
              `language`,
              `info_source`,
              `spider`
              ) VALUES (
              '{item["title"]}',
              '{item["director"]}',
             '{item["actor"]}',
             '{item["duration"]}',
             '{item["movie_image"]}',
             '{item["rating"]}',
             '{item["release_date"]}',
             '{item["type"]}',
             '{item["language"]}',
             '{item["info_source"]}',
             '{spider.name}'
              );
              """
            self.cursor.execute(insert_sql)
            self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()