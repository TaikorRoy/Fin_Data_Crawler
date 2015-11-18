from ..lib.es_driver import post_to_es
from ..lib.es_driver import construct_es_url


class PY_TEMPLATE(object):
    def __init__(self):
        self.crawling_time = None
        self.source_name = None
        self.crawl_id = None
        self.data_id = None
        self.es_doc = None

        # TODO: Define Spider Specific Class Attributes

    def crawl(self, job):
        # TODO: Define or Call Spider Specific Methods to start the Crawling & Parsing Process
        pass

    def push_to_db(self):
        # The code to use when post to ES
        base_url = construct_es_url()
        url_var = ""
        # TODO: Provide the value of url_var
        es_url = base_url + url_var
        post_to_es(es_url, self.es_doc)

    def logging(self):
        pass

    def sleep(self):
        pass

    # TODO: Define Spider Specific Class Methods
