from fin_data_crawler.lib.mysql_driver import MySQLdriver
from fin_data_crawler.config import mysql_host, username, pw, db
from fin_data_crawler.lib.util import get_formated_time_mysql
from fin_data_crawler.lib.util import toshare_null_handle
import tushare as ts
from fin_data_crawler.lib.util import json_to_mysql
import time
import uuid


class crawler(object):
    def __init__(self):
        self.source_name = "toshare"
        self.crawl_id = "PYts0001"
        self.data = list()

        self.table = "profitability_ratios"
        self.global_sync_year_start = 1989
        self.global_sync_season_enum = {1, 2, 3, 4}

    def crawl(self, job):
        if job == "sync":
            self.sync()
        if job == "global_sync":
            self.global_sync()

    def push_to_db(self):
        # The code to use when post to ES
        mysql = MySQLdriver(mysql_host, username, pw, db)
        for item in self.data:
            try:
                check_sql = json_to_mysql(item, self.table, "select")
                result = mysql.check_records(check_sql)
                if result is False:
                    insert_sql = json_to_mysql(item, self.table, "insert")
                    mysql.insert(insert_sql)
            except:
                print(insert_sql)
                print(item)
        mysql.clean_up()

    def logging(self):
        pass

    def sleep(self):
        pass

    def sync(self):
        struct_time = time.localtime()
        year = struct_time.tm_year
        month = struct_time.tm_mon
        season = int(month/4)

        self.get_data_by_year_season(year, season)

    def global_sync(self):
        struct_time = time.localtime()
        current_year = struct_time.tm_year
        year_enum = range(self.global_sync_year_start, current_year + 1)

        for year in year_enum:
            for mon in self.global_sync_season_enum:
                self.get_data_by_year_season(year, mon)

    def get_data_by_year_season(self, year, season):
        struct_time = time.localtime()
        current_year = struct_time.tm_year
        current_month = struct_time.tm_mon

        df = ts.get_profit_data(year, season)
        if df is not None:
            if df.empty is False:
                n_data = len(df.index)
                for i in range(n_data):
                    data = df.iloc[i]
                    data_json = {
                    "id": uuid.uuid4().hex,
                    "code": data["code"],
                    "datetime": str(current_year) + "-" + str(current_month) + "-" + "00" + " " + "00" + ":" + "00" + ":" + "00",
                    "fetchtime": get_formated_time_mysql(),
                    "source": self.source_name,
                    "crawler": self.crawl_id,
                    "ROE": data["roe"],
                    "NPMOS": data["net_profit_ratio"],
                    "GPTS": data["gross_profit_rate"],
                    "IFMO": data["net_profits"],
                    "DOE": data["eps"],
                    }

                    data_json = toshare_null_handle(data_json)
                    self.data.append(data_json)



