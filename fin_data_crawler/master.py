__author__ = 'roy'
from config import spider_ready


class master(object):
    def __init__(self, job_manager, _spiders):
        self.tm = job_manager
        self.spiders = _spiders

    def wake_up_spider(self, _id):
        return self.spiders[_id]

    def start_main_loop(self):
        while True:
            signal, spider_id, job = self.tm()
            if signal:
                spider = self.wake_up_spider(spider_id)
                spider.crawl(job)
                spider.push_to_db()
                spider.logging()
                spider.sleep()
