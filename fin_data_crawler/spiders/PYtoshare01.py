from fin_data_crawler.lib.mysql_driver import MySQLdriver
from string import Template
from fin_data_crawler.config import mysql_host, username, pw, db
from fin_data_crawler.lib.util import get_formated_time
import tushare as ts
import time
import uuid


class PYtoshare01(object):
    def __init__(self):
        self.source_name = "toshare"
        self.crawl_id = "PYtoshare01"
        self.data = list()

        self.sqls = list()

    def crawl(self, job):
        if job == "sync":
            self.sync()

    def push_to_db(self):
        # The code to use when post to ES
        mysql = MySQLdriver(mysql_host, username, pw, db)
        for sql in self.sqls:
            mysql.insert(sql)
        mysql.clean_up()

    def logging(self):
        pass

    def sleep(self):
        pass

    def sync(self):
        struct_time = time.localtime()
        year = struct_time.tm_year
        month = struct_time.tm_mon
        df = ts.get_profit_data(year, month)

        n_data = df.rows

        for i in range(n_data):
            data = df.loc(i)
            data_json = {
            "id": uuid.uuid4().hex,
            "code": data("code"),
            "datetime": str(year) + "-" + str(month) + "-" + str(00) + "T" + str(00) + ":" + str(00) + ":" + str(00) + "+08:00",
            "fetchtime": get_formated_time(),
            "source": self.source_name,
            "crawler": self.crawl_id,
            "ROE": data("roe"),
            "NPMOS": data("net_profit_ratio"),
            "GPTS": data("gross_profit_rate"),
            "IFMO": data("net_profits"),
            "DOE": data("eps"),
            }
            self.data.append(data)




