from rsser import FeedParser
from content_db import ContentDB
from addr_db import AddressesDB
from rss_logger import server_logger


class RSSManager(object):
    def __init__(self):
        self._contentDb = ContentDB()
        self._addressesDb = AddressesDB()
        self._feedParser = FeedParser()

    def add_new_address(self, url):
        server_logger.debug(f'{url} added to the database')
        self._addressesDb.insert_one(url)

    def remove_address(self, url):
        self._addressesDb.remove(url)

    def get_feed(self):
        return self._contentDb.get_feed()

    def get_feeds_by_dates(self, start_date, end_date):
        return [doc for doc in self._contentDb.search_by_dates(start_date, end_date)]

    def search_content(self, keywords):
        return [doc for doc in self._contentDb.search(keywords)]

    def update_feed(self):
        # Batching in order to support scale
        urls = [url for url in self._addressesDb.get_addresses()]
        server_logger.debug(f'URLs list: {urls}')
        for feed in self._feedParser.parse_many(urls):
            server_logger.debug(f'feed: {feed}')
            for entry in feed.entries:
                server_logger.debug(entry)
                self._contentDb.insert_one(entry)


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

    rss_mng = RSSManager()
    # rss_mng._contentDb.remove_all()
    # [rss_mng.remove_address(url) for url in rss_list]
    # [rss_mng.add_new_address(url) for url in rss_list]
    # rss_mng.update_feed()
    # for doc in rss_mng.get_feed():
    #     print(doc)
    # print('by dates')
    # # Year.Month.Day
    # [print(d) for d in rss_mng.get_feeds_by_dates('2018.11.10', '2018.12.01')]
    # print('by dates flase')
    # # Year.Month.Day
    # [print(d) for d in rss_mng.get_feeds_by_dates('2019.11.10', '2019.12.01')]
    print([d for d in rss_mng.search_content('turkey')])