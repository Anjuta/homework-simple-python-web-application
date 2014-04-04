__author__ = 'SONY'

import shelve, time

class DataBase(object):
    DATA_BASE = 'data_base.db'

    def __init__(self):
        self.db = shelve.open(self.DATA_BASE)

    def add_review(self, site_name, review):
        if site_name != '':
            date = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
            if site_name in self.db.keys():
                reviews = self.db[site_name]
            else:
                reviews = []
            reviews.insert(0, date + ' ~ ' + review)
            self.db[site_name] = reviews
        self.db.sync()

    def get_all_sites(self):
        return self.db.keys()

    def get_reviews_on_site(self, site_name):
        return self.db[site_name] if site_name in self.db.keys() else None

