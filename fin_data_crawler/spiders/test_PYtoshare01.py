__author__ = 'roy'

import fin_data_crawler.spiders.PYtoshare01
crawler = fin_data_crawler.spiders.PYtoshare01.PYtoshare01()

job = "sync"
crawler.crawl(job)
crawler.push_to_db()
