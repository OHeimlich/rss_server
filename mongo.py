import pymongo
from rss_logger import server_logger

rss_db_client = pymongo.MongoClient("mongodb://localhost:27017/")
rss_db = rss_db_client["rss_database"]

rss_addr = rss_db['rss_addresses']
rss_content = rss_db['rss_content']
server_logger.debug(rss_db.list_collection_names())
