Dependencies:
1. pymongo - A MongoDB driver module.
2. feedparser - A RSS feeds parser.
3. MongoDB database.

TODO:
- Add unit tests.
- Add documentation.

Data entry example:

{'title': "Jamal Khashoggi murder: Turkey 'shared tapes' with Saudi, US",
 'title_detail': {'type': 'text/plain', 'language': None, 'base': 'http://feeds.bbci.co.uk/news/world/rss.xml', 'value': "Jamal Khashoggi murder: Turkey 'shared tapes' with Saudi, US"},
 'summary': "Turkey's president says he has shared recordings of the murder of the writer with the US, UK and Saudis.",
 'summary_detail': {'type': 'text/html', 'language': None, 'base': 'http://feeds.bbci.co.uk/news/world/rss.xml', 'value': "Turkey's president says he has shared recordings of the murder of the writer with the US, UK and Saudis."},
 'links': [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://www.bbc.co.uk/news/world-europe-46162759'}],
 'link': 'https://www.bbc.co.uk/news/world-europe-46162759',
 'id': 'https://www.bbc.co.uk/news/world-europe-46162759',
 'guidislink': False,
 'published': 'Sat, 10 Nov 2018 14:50:23 GMT',
 'published_parsed': time.struct_time(tm_year=2018, tm_mon=11, tm_mday=10, tm_hour=14, tm_min=50, tm_sec=23, tm_wday=5, tm_yday=314, tm_isdst=0),
 'media_thumbnail': [{'width': '976', 'height': '549', 'url': "http://c.files.bbci.co.uk/D7FE/production/_104149255_khashoggi'sfriendsaroundtheworld.jpg"}],
 'href': ''}