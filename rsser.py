import feedparser
from multiprocessing import Process, Queue
from rss_logger import server_logger


class FeedParser(object):
    '''
    RSS Feed parser
    '''
    def __init__(self):
        self.feeds_queue = Queue()

    def parse_one(self, url, q=None):
        '''
        Parse single RSS url
        :param url: URL to the RSS server
        :param q: If not None push the data into the queue
        :return: If not None returns the RSS data
        '''
        server_logger.info(f'Parsing: {url}')
        data = feedparser.parse(url)
        server_logger.debug(f'Finish to read rss data ({url})')
        if data.status is not 200:
            raise NameError(f'Error! could not get data from the server error code: {data.status}')

        if q:
            q.put(data)
            server_logger.debug(f'{data}: data is in the queue')
        else:
            return data

    def parse_many(self, urls_list):
        '''
        Multiprocessing RSS, push the RSS content into the class queue
        :param urls_list: List of URL to process
        :return: None
        '''
        processes = []
        for url in urls_list:
            p = Process(target=self.parse_one, args=(url, self.feeds_queue))
            p.start()
            processes.append(p)

        [p.join(timeout=3) for p in processes]

        while not self.feeds_queue.empty():
            yield self.feeds_queue.get()

        [p.terminate() for p in processes]


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

    fp = FeedParser()
    adr_l = [url['address'] for url in rss_list]
    print(adr_l)

    [print(addr) for addr in fp.parse_many(adr_l)]
