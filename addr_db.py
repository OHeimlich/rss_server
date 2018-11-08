from mongo import rss_addr


class AddressesDB(object):
    '''
    RSS addresses (URL) MongoDB database
    '''
    def __init__(self):
        self._db = rss_addr

    def insert_one(self, url):
        # TODO: Validate the URL
        doc = {'address': url}
        if self._db.find_one(doc):
            raise NameError(f'Address: {doc["address"]} already exist!')
        self._db.insert_one(document=doc)

    def insert_many(self, urls_list):
        if urls_list.__class__ is list:
            for url in urls_list:
                self.insert_one(url)
        else:
            self.insert_one(urls_list)

    def get_addresses(self, filter={}):
        for doc in self._db.find(filter):
            yield doc['address']

    def remove(self, url):
        doc = {'address': url}
        if not self._db.find_one(doc):
            raise NameError(f'Address: {url} does not exist!')
        self._db.delete_one(doc)


if __name__ == '__main__':
    rss_list = ['http://feeds.bbci.co.uk/news/world/rss.xml',
                'http://feeds.bbci.co.uk/news/business/rss.xml',
                'http://feeds.reuters.com/Reuters/worldNews',
                'https://www.dailytelegraph.com.au/help-rss',
                'http://www.weatherzone.com.au/services/rss.jsp',
                'https://thewest.com.au/rss-feeds',
                'http://feeds.bbci.co.uk/news/rss.xml',
                'http://www.cbn.com/cbnnews/us/feed/',
                'http://feeds.reuters.com/Reuters/domesticNews',
                'http://news.yahoo.com/rss/']
    db = AddressesDB()

    [db.remove(doc) for doc in rss_list]
    [print(doc) for doc in db.get_addresses()]

    db.insert_one(rss_list[0])
    [print(doc) for doc in db.get_addresses()]
    db.insert_many(rss_list[1:])
    [print(doc) for doc in db.get_addresses()]
