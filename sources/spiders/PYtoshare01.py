from ..lib.es_driver import ESdriver
from ..lib.mysql_driver import MySQLdriver
from string import Template
import tushare as ts
import time


class PY_TEMPLATE(object):
    def __init__(self):
        self.crawling_time = None
        self.source_name = None
        self.crawl_id = None
        self.data_id = None
        self.es_doc = None
        self.data = None

        # TODO: Define Spider Specific Class Attributes

    def crawl(self, job):
        # TODO: Define or Call Spider Specific Methods to start the Crawling & Parsing Process
        pass

    def push_to_db(self):
        # The code to use when post to ES
        es = ESdriver()
        # TODO: Provide the necessary arugment to ESdriver()
        es.post_to_es(self.data)

    def logging(self):
        pass

    def sleep(self):
        pass

    # TODO: Define Spider Specific Class Methods


def download_tushare():
    struct_time = time.localtime()
    year = struct_time.tm_year
    month = struct_time.tm_mon
    df = ts.get_profit_data(year, month)

    n_data = df.rows

    for i in range(n_data):
        data = df.loc(i)
        data_json = {
        "code": data("code"),
        "data_name": data("name"),
        "data_roe": data("roe"),
        "data_net_profit_ratio": data("net_profit_ratio"),
        "data_gross_profit_rate": data("gross_profit_rate"),
        "data_net_profits": data("net_profits"),
        "data_eps": data("eps"),
        "data_business_income": data("business_income"),
        "data_bips": data("bips")
        }




