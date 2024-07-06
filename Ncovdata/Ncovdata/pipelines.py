# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
import json

class NcovdataPipeline:
    # 文件名
    current_date_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    def process_item(self, item, spider):
        print("管道输入：", item)
        with open('./data/{}.txt'.format(self.current_date_str), mode='a', encoding='utf8') as file:
            file.write(json.dumps(item, ensure_ascii=False)) # 禁用中文编码
            file.write('\n')

        return item
