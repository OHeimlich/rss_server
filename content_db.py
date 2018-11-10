import pymongo
from mongo import rss_content
from datetime import datetime

class ContentDB(object):
    '''
    RSS Content MongoDB database
    '''
    def __init__(self):
        self._db = rss_content
        self._db.create_index([('title', pymongo.TEXT), ('link', pymongo.TEXT)])

    def insert_one(self, doc):
        # TODO: Validate the document and deal with duplications
        self._db.insert_one(document=doc)

    def insert_many(self, docs_list):
        if docs_list.__class__ is list:
            for doc in docs_list:
                self.insert_one(doc)
        else:
            self.insert_one(docs_list)

    def get_feed(self, filter={}):
        for doc in self._db.find(filter):
            yield doc

    def remove(self, doc):
        if not self._db.find_one({'title': doc['title']}):
            raise NameError(f'Title: "{doc["title"]}" does not exist!')
        self._db.delete_one({'title': doc['title']})

    def remove_all(self):
        self._db.remove()

    def search(self, keywords):
        return self._db.find({"$text": {"$search": keywords}})

    # def compare
    def search_by_dates(self, start_date, end_date):
        s_t = start_date.split('.')
        s_t = [int(i) for i in s_t]
        e_t = end_date.split('.')
        e_t = [int(i) for i in e_t]
        return self._db.find({'published_parsed': {'$gte': s_t, '$lt': e_t}})
