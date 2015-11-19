from ..lib.es_driver import ESdriver
from ..lib.mysql_driver import MySQLdriver


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
