from fin_data_crawler.lib.es_driver import ESdriver
from fin_data_crawler.lib.mysql_driver import MySQLdriver


class PY_TEMPLATE(object):
    def __init__(self):
        self.source_name = None
        self.crawl_id = None
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
