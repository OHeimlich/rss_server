from mongo import rss_content


class ContentDB(object):
    '''
    RSS Content MongoDB database
    '''
    def __init__(self):
        self._db = rss_content

    def insert_one(self, doc):
        # TODO: Validate the document
        if self._db.find_one({'address': doc['address']}):
            raise NameError(f'Address: {doc["address"]} already exist!')
        self._db.insert_one(document=doc)

    def insert_many(self, docs_list):
        if docs_list.__class__ is list:
            for doc in docs_list:
                self.insert_one(doc)
        else:
            self.insert_one(docs_list)

    def get_addresses(self, filter={}):
        for doc in self._db.find(filter):
            yield doc

    def remove(self, doc):
        if not self._db.find_one({'address': doc['address']}):
            raise NameError(f'Address: {doc["address"]} does not exist!')
        self._db.delete_one({'address': doc['address']})
