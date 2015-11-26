from ..lib.es_driver import ESdriver
from ..lib.mysql_driver import MySQLdriver
from string import Template
from ..lib.util import get_formated_time
import tushare as ts
import time
import uuid


class PY_TEMPLATE(object):
    def __init__(self):
        self.source_name = "toshare"
        self.crawl_id = "PYtoshare01"
        self.data = list()

    def crawl(self, job):
        if job == "sync":
            self.sync()

    def push_to_db(self):
        # The code to use when post to ES
        es = ESdriver()
        for item in self.data:
            es.post_to_es(item)

    def logging(self):
        pass

    def sleep(self):
        pass

    def sync(self):
        id_generator = uuid()
        struct_time = time.localtime()
        year = struct_time.tm_year
        month = struct_time.tm_mon
        df = ts.get_profit_data(year, month)

        n_data = df.rows

        for i in range(n_data):
            data = df.loc(i)
            data_json = {
            "id": id_generator.uuid4(),
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




