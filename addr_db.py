from mongo import rss_addr


class AddressesDB(object):
    '''
    RSS addresses (URL) MongoDB database
    '''
    def __init__(self):
        self._db = rss_addr

    def insert_one(self, doc):
        # TODO: Validate the URL
        if self._db.find_one(doc):
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
        if not self._db.find_one(doc):
            raise NameError(f'Address: {doc["address"]} does not exist!')
        self._db.delete_one(doc)


if __name__ == '__main__':
    rss_list = [{'address': 'http://feeds.bbci.co.uk/news/world/rss.xml'},
                {'address': 'http://feeds.bbci.co.uk/news/business/rss.xml'},
                {'address': 'http://feeds.reuters.com/Reuters/worldNews'},
                {'address': 'https://www.dailytelegraph.com.au/help-rss'},
                {'address': 'http://www.weatherzone.com.au/services/rss.jsp'},
                {'address': 'https://thewest.com.au/rss-feeds'},
                {'address': 'http://feeds.bbci.co.uk/news/rss.xml'},
                {'address': 'http://www.cbn.com/cbnnews/us/feed/'},
                {'address': 'http://feeds.reuters.com/Reuters/domesticNews'},
                {'address': 'http://news.yahoo.com/rss/'}]
    db = AddressesDB()

    [db.remove(doc) for doc in rss_list]
    [print(doc) for doc in db.get_addresses()]

    db.insert_one(rss_list[0])
    [print(doc) for doc in db.get_addresses()]
    db.insert_many(rss_list[1:])
    [print(doc) for doc in db.get_addresses()]
